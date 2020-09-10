#TODO: Comments and refactor
import json
import os
import git
from py3_api_doc import generate_documentation_from_xml
import ftplib
import subprocess
import argparse
from pathlib import Path


class Repo:
    def __init__(self, path, name):
        self.path = path
        self.name = name

        with open(path + '/documentation_config.json') as f:
            config = json.load(f)
            self.is_main_repo = config['is_main_repo']
            self.part_of = config['part_of']
            self.contains_py_api = config['contains_py_api']

            if self.is_main_repo:
                with open(path + '/introduction.md') as f:
                    self.introduction = f.read()

            if self.contains_py_api:
                self.py_api_xml_name = config['py_api_xml_name']
            self.exclude = config['exclude']


def add_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def generate_py_api(repo, ftp_user, ftp_pass):
    ftp = ftplib.FTP('')
    ftp.connect('simplic.biz', 22)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    ftp.cwd('/.net-xml-doc')

    ftp.retrbinary(f'RETR {repo.py_api_xml_name}', open(f'xml/{repo.py_api_xml_name}', 'wb').write)
    ftp.quit()

    if repo.part_of == 'core':
        add_dir('../api_core/api_python')
        generate_documentation_from_xml(f'xml/{repo.py_api_xml_name}',
                      f'../api_core/api_python')
    else:
        add_dir(f'../api_plugins/{repo.part_of}')
        add_dir(f'../api_plugins/{repo.part_of}/api_python')
        generate_documentation_from_xml(f'xml/{repo.py_api_xml_name}',
                      f'../api_plugins/{repo.part_of}/api_python')
   
    print(f'Generated Python API files for {repo.name}')
    os.remove(f'xml/{repo.py_api_xml_name}')

# Writes the toc for code_samples and api_python dirs
def write_subdirectories_toc():
    markdown_dirs = [_dir for _dir in Path('../').rglob('') if str(_dir).endswith(('code_samples', 'api_python'))]
    for _dir in markdown_dirs:
        with open(Path(f'{_dir}/toc.yml'), 'w+') as f:
            # Generate toc based of markdown files in directory
            toc = ''.join([f'- name: {_f[:-3]}\n  href: {_f}\n' for _f in os.listdir(_dir) if _f.endswith('.md')])
            f.write(toc)


class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print (f'{op_code}, {cur_count}, {max_count},{message}')

parser = argparse.ArgumentParser()
parser.add_argument('--git-user', help='Your GitHub username')
parser.add_argument('--git-pass', help='Your GitHub password')
parser.add_argument('--ftp-user', help='The ftp username')
parser.add_argument('--ftp-pass', help='The ftp password')
args = vars(parser.parse_args())

git_user = args['git_user']
git_pass = args['git_pass']
ftp_user = args['ftp_user']
ftp_pass = args['ftp_pass']


if not all([git_user, git_pass, ftp_user, ftp_pass]):
    print('Enter all Arguments. Get a list of the arguments by adding --help to the script call. e.g. python build.py --help')
    exit()

docfx = {}

with open('../docfx.json', 'r') as f:
    docfx = json.load(f)

with open('repositories.json') as f:
    repo_links = json.load(f)['links']

add_dir('clones')
add_dir('xml')

for i, link in enumerate(repo_links):
    repo_name = link.split('/simplic/')[1]
    dest = 'clones/' + repo_name
    try:
        authed_link = link.replace('github.com', f'{git_user}:{git_pass}@github.com')
        git.Repo.clone_from(authed_link, dest, branch='master')
    except git.exc.GitCommandError as e: # git.exc.GitCommandError
        print(str(e))

    repo = Repo(dest, repo_name)
    files = [f'build/{dest}/src/**.csproj']
    if repo.name in ['simplic-service.git', 'Simplic-Import-Tyre24.git', 'simplic-change-tracking.git']:
        files = [f'build/{dest}/**.csproj']
    
    # If associated plugin is already in metadata, append to it
    for m in docfx['metadata']:
        if repo.part_of in m['dest']:
            m['src']['files'] += files
            m['src']['exclude'] += repo.exclude
            break
    else:
        if repo.part_of == 'core':
            metadata = {'src': {'files': files, 'exclude': repo.exclude},
                'dest': 'api_core/api','filter': 'filter.yml'}
        else:
            metadata = {'src': {'files': files, 'exclude': repo.exclude},
            'dest': f'api_plugins/{repo.part_of}/api', 'filter': 'filter.yml'}
        docfx['metadata'].append(metadata)
    
    if repo.contains_py_api:
        try:
            generate_py_api(repo, ftp_user, ftp_pass)
        except Exception as e:
            print(f'Exception when generating py_api for {repo.name}:\n{str(e)}')

    # Save Introduction
    if repo.is_main_repo and repo.part_of == 'core':
        with open('../api_core/getting_started/introduction.md', 'w+') as f:
            f.write(repo.introduction)
    elif repo.is_main_repo and repo.part_of != 'core':
        add_dir(f'../api_plugins/{repo.part_of}')
        with open(f'../api_plugins/{repo.part_of}/introduction.md', 'w+') as f:
            f.write(repo.introduction)
    
    print(f'Just added {repo.name} to metadata. {i+1} out of {len(repo_links)} done.')

write_subdirectories_toc()

with open('../docfx.json', 'w+') as f:
    json.dump(docfx, f)
p = subprocess.Popen(['docfx', '--metadata'], cwd='../')
p.wait()
with open('../docfx.json', 'w+') as f:
    docfx['metadata'] = []
    json.dump(docfx, f)


# write api_plugin and api_plugin/* toc
api_plugins_toc = ''
plugins = [f for f in os.listdir('../api_plugins') if os.path.isdir(f'../api_plugins/{f}')]
for plugin in plugins:
    plugin_toc = '- name: Introduction\n  href: introduction.md\n'
    if os.path.exists(f'../api_plugins/{plugin}/code_samples'):
        plugin_toc += '- name: Code Samples\n  href: code_samples/toc.yml\n'
    if os.path.exists(f'../api_plugins/{plugin}/api'):
        plugin_toc += '- name: Reference\n  href: api/toc.yml\n'
    if os.path.exists(f'../api_plugins/{plugin}/api_python'):
        plugin_toc += '- name: Python Reference\n  href: api_python/toc.yml\n'
    api_plugins_toc += f'- name: {plugin}\n  href: {plugin}/toc.yml\n  homepage: {plugin}/introduction.md\n'

    with open(f'../api_plugins/{plugin}/toc.yml', 'w+') as f:
        f.write(plugin_toc)

with open('../api_plugins/toc.yml', 'w+') as f:
    f.write(api_plugins_toc)
