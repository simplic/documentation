import json
from github import Github, GithubException
from itertools import groupby
import os
from pathlib import Path
import lxml.etree as ET
from enum import Enum
import argparse

# variables with underscores contain xml elements
class MainModule:
    def __init__(self, name, master_release_notes, dev_release_notes, user_master_release_notes, user_dev_release_notes):
        self.name = name
        self.master_release_notes = master_release_notes
        self.dev_release_notes = dev_release_notes
        self.user_master_release_notes = user_master_release_notes
        self.user_dev_release_notes = user_dev_release_notes

        self.submodules = []

    def __repr__(self):
        return f'(Name: {self.name}, Submodules: {self.submodules})'

class SubModule:
    def __init__(self, name, master_release_notes, dev_release_notes):
        self.name = name
        self.master_release_notes = master_release_notes
        self.dev_release_notes = dev_release_notes
    
    def __repr__(self):
        return f'(Name: {self.name})'

class MasterReleaseNotes:
    def __init__(self, xml):
        root = ET.fromstring(xml)
        self.change_sets = [ChangeSet(_change_set) for _change_set in root if _change_set.get('version')]
        self.change_sets.sort(key=lambda x: (x.version.split('.')[0], x.version.split('.')[1], x.version.split('.')[2][:-2]), reverse=True)

    def get_latest_version_number(self):
        if self.change_sets:
            return self.change_sets[0].version
        else:
            return None

    def get_latest_change_sets(self):
        return self.get_change_sets_with_version(self.get_latest_version_number())

    def get_change_sets_with_version(self, version):
        return [change_set for change_set in self.change_sets if change_set.version == version]

class DevReleaseNotes:
    def __init__(self, xml, master_release_notes):
        root = ET.fromstring(xml)
        self.change_sets = [ChangeSet(_change_set) for _change_set in root]

        self.upcoming_change_sets = []
        for change_set in self.change_sets:
            if not any([master_change_set for master_change_set in master_release_notes.change_sets if
                        master_change_set.guid == change_set.guid]):
                self.upcoming_change_sets.append(change_set)

class ChangeSet:
    def __init__(self, _change_set):
        self.version = _change_set.get('version')
        self.date = _change_set.get('date')
        self.guid = _change_set.get('guid')

        # assert self.guid is not None

        self.changes = [Change(_change) for _change in _change_set]

    def to_markdown(self, release_note_type, show_version):
        if release_note_type == ReleaseNoteType.Dev:
            markdown = ''
            if show_version and self.version and self.date:
                markdown += f'`Version: {self.version}, '
                markdown += f'Date: {self.date}`\n'
                markdown += '---\n'

            features = [c for c in self.changes if c.type == 'feature']
            enhancements = [c for c in self.changes if c.type == 'enhancement']
            bug_fixes = [c for c in self.changes if c.type == 'bug']

            if features:
                markdown += '**Features**\n'
                for feature in features:
                    markdown += f'* {feature.text}\n'

            if enhancements:
                if features:
                    markdown += '\n'
                markdown += '**Enhancements**\n'
                for enhancement in enhancements:
                    markdown += f'* {enhancement.text}\n'

            if bug_fixes:
                if features or enhancements:
                    markdown += '\n'
                markdown += '**Bug fixes**\n'
                for bug_fix in bug_fixes:
                    markdown += f'* {bug_fix.text}\n'

            return markdown
        elif release_note_type == ReleaseNoteType.User:
            return self.to_markdown(ReleaseNoteType.Dev, True) # TODO

    # Aggregate multiple ChangeSet's as one with this
    # Careful! This removes the guid of the added change set completely. Only use for writing change_sets to file!
    def __add__(self, other):
        if self.version == other.version:
            change_set = ChangeSet(ET.fromstring('<xml></xml>'))
            change_set.version = self.version
            change_set.guid = self.guid
            change_set.date = self.date
            change_set.changes = self.changes + other.changes
            return change_set
        else:
            print('Couldent aggregate change sets.')

    def __radd__(self, other):
        if not other:
            return self
        else:
            return self.__add__(other)

    def __len__(self):
        return len(self.changes)

    def __repr__(self):
        return f'(Version: {self.version}, Date: {self.date}, Guid: {self.guid}, Changes: {len(self)}'

class Change:
    def __init__(self, _change):
        self.type = _change.get('type')
        self.text = _change.text.strip()

class ReleaseNoteType(Enum):
    User = 1
    Support = 2
    Dev = 3

def write_latest_release_notes(main_modules, release_note_type):
    if release_note_type == ReleaseNoteType.User:
        with open('../user/index.md', 'a+') as f:
            write_line(f, '# Latest Changes')

            for main_module in main_modules:
                latest_change_sets = main_module.user_master_release_notes.get_latest_change_sets()

                if latest_change_sets:
                    write_line(f, f'## [{main_module.name}]({main_module.name.replace(" ", "%20")}.md)')
                    latest_change_set = aggregated_change_sets(latest_change_sets)[0]
                    write_line(f, latest_change_set.to_markdown(ReleaseNoteType.User, True))
                    write_line(f, '---')

            write_line(f, '# Upcoming Changes')
            
            for main_module in main_modules:
                upcoming_change_sets = main_module.user_dev_release_notes.upcoming_change_sets

                if upcoming_change_sets:
                    write_line(f, f'## [{main_module.name.replace}]({main_module.name.replace(" ", "%20")}.md)')
                    upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]
                    write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.User, False))
                    write_line(f, '---')

    elif release_note_type == ReleaseNoteType.Dev:
        with open('../dev/index.md', 'a+') as f:
            write_line(f, '# Latest Changes')

            for main_module in main_modules:
                latest_version_number = main_module.master_release_notes.get_latest_version_number()
                latest_change_sets = main_module.master_release_notes.get_latest_change_sets()

                if latest_change_sets or any([submodule.master_release_notes.get_change_sets_with_version(latest_version_number) for submodule in main_module.submodules]):
                    write_line(f, f'## [{main_module.name}]({main_module.name.replace(" ", "%20")}/1main.md)')

                    if latest_change_sets:
                        latest_change_set = aggregated_change_sets(latest_change_sets)[0]
                        write_line(f, latest_change_set.to_markdown(ReleaseNoteType.Dev, True))
                
                    write_line(f, '---')

                for submodule in main_module.submodules:
                    change_sets_with_version = submodule.master_release_notes.get_change_sets_with_version(latest_version_number)

                    if change_sets_with_version:
                        write_line(f, f'#### [{submodule.name}]({main_module.name.replace(" ", "%20")}/{submodule.name.replace(" ", "%20")}.md)')
                        change_set = aggregated_change_sets(change_sets_with_version)[0]
                        
                        write_line(f, change_set.to_markdown(ReleaseNoteType.Dev, False))
                        write_line(f, '---')
            
            write_line(f, '# Upcoming Changes')
            for main_module in main_modules:
                upcoming_change_sets = main_module.dev_release_notes.upcoming_change_sets

                if upcoming_change_sets or any([submodule.dev_release_notes.upcoming_change_sets for submodule in main_module.submodules]):
                    write_line(f, f'## [{main_module.name}]({main_module.name.replace(" ", "%20")}/1main.md)')

                    if upcoming_change_sets:
                        upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]
                        write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.Dev, False))
                
                    write_line(f, '---')

                for submodule in main_module.submodules:
                    upcoming_change_sets = submodule.dev_release_notes.upcoming_change_sets

                    if upcoming_change_sets:
                        write_line(f, f'#### [{submodule.name}]({main_module.name.replace(" ", "%20")}/{submodule.name.replace(" ", "%20")}.md)')
                        upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]

                        write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.Dev, False))
                        write_line(f, '---')


def write_release_notes(main_module, release_note_type):
    if release_note_type == ReleaseNoteType.User:
        with open(f'../user/{main_module.name}.md', 'a+') as f:
            change_sets = main_module.user_master_release_notes.change_sets
            
            write_line(f, '# Release Notes')

            for change_set in aggregated_change_sets(change_sets):
                write_line(f, change_set.to_markdown(ReleaseNoteType.User, True))
                write_line(f, '---')

    elif release_note_type == ReleaseNoteType.Dev:
        dir_path = Path(f'../dev/{main_module.name}')
        if not dir_path.exists():
            os.mkdir(dir_path)

        with open(f'{dir_path}/1main.md', 'a+') as f:
            change_sets = main_module.master_release_notes.change_sets
            
            write_line(f, '# Release Notes')

            for change_set in aggregated_change_sets(change_sets):
                write_line(f, change_set.to_markdown(ReleaseNoteType.Dev, True))
                write_line(f, '---')

        for submodule in main_module.submodules:
            with open(f'{dir_path}/{submodule.name}.md', 'a+') as _f:
                write_line(_f, '# Release Notes')

                change_sets = submodule.master_release_notes.change_sets

                for change_set in aggregated_change_sets(change_sets):
                    write_line(_f, change_set.to_markdown(ReleaseNoteType.Dev, True))
                    write_line(_f, '---')

def write_line(file, string):
    file.write(f'{string}\n')

def aggregated_change_sets(unaggregated_change_sets):
    return [sum(list(change_set_group)) for _, change_set_group in groupby(unaggregated_change_sets, key=lambda x: x.version)]

def write_toc(release_note_type):
    if release_note_type == ReleaseNoteType.User:
        # Write toc for ../user
        with open('../user/toc.yml', 'a+') as f:
            toc = ''
            for _f in os.listdir('../user'):
                if _f.endswith('.md'):
                    if _f == 'index.md':
                        toc += f'- name: Latest Changes\n  href: {_f}\n'
                    else:
                        toc += f'- name: {_f[:-3]}\n  href: {_f}\n'
            f.write(toc)

    elif release_note_type == ReleaseNoteType.Dev:
        # Write toc for all modules
        for dir in Path('../dev').rglob(''):
            with open(f'{dir}/toc.yml', 'a+') as f:
                toc = ''
                for _f in os.listdir(dir):
                    if _f.endswith('.md'):
                        if _f == '1main.md':
                            toc += f'- name: Main Module\n  href: {_f}\n'
                        else:
                            toc += f'- name: {_f[:-3]}\n  href: {_f}\n'
                f.write(toc)
        # Write ../dev toc
        with open(f'../dev/toc.yml', 'w+') as f:
            toc = ''
            for _f in os.listdir('../dev'):
                if _f == 'index.md':
                    toc += f'- name: Latest Changes\n  href: {_f}\n'
                elif _f != 'toc.yml':
                    toc += f'- name: {_f}\n  href: {_f}/toc.yml\n  homepage: {_f}/1main.md\n'
            f.write(toc)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--git-user', help='Your GitHub username')
    parser.add_argument('--git-pass', help='Your GitHub password')
    args = vars(parser.parse_args())

    git_user = args['git_user']
    git_pass = args['git_pass']

    if not git_user or not git_pass:
        print('Enter all Arguments. Get a list of the arguments by adding --help to the script call. e.g. python build.py --help')
        exit()

    g = Github(git_user, git_pass)
    org = g.get_organization('simplic')
    
    main_modules = []

    main_repositories = json.loads(Path('main_repositories.json').read_text())

    for link in main_repositories['links']:
        repo_name = link.split('/simplic/')[1]
        dir = Path(f'../../dev/build/clones/{repo_name}')
        if dir.exists():
            documentation_config = json.loads(Path(f'{dir}/documentation_config.json').read_text())
            infrastructure = json.loads(Path(f'{dir}/infrastructure.json').read_text())

            module_name = documentation_config['part_of'] if documentation_config['part_of'] != 'core' else 'Simplic Studio'

            if Path(f'{dir}/release-notes.xml').exists():
                master_release_notes_xml = Path(f'{dir}/release-notes.xml').read_text()

                remote_repo = org.get_repo(dir.name.replace('.git', ''))
                try:
                    dev_release_notes_xml = remote_repo.get_contents('release-notes.xml', ref='dev').decoded_content
                except GithubException:
                    dev_release_notes_xml = '<ReleaseNotes></ReleaseNotes>'
                    print(f'{dir.name.replace(".git", "")} has no release-notes.xml in dev') 
                
                    master_release_notes = MasterReleaseNotes(master_release_notes_xml)
                    dev_release_notes = DevReleaseNotes(dev_release_notes_xml, master_release_notes)

                try:
                    user_master_release_notes_xml = Path(f'{dir}/user-release-notes.xml')
                    user_dev_release_notes_xml = remote_repo.get_contents('user-release-notes.xml', ref='dev').decoded_content
                    user_master_release_notes = MasterReleaseNotes(user_master_release_notes_xml)
                    user_dev_release_notes = DevReleaseNotes(user_dev_release_notes_xml, user_master_release_notes)
                except:
                    user_master_release_notes = MasterReleaseNotes('<ReleaseNotes></ReleaseNotes>')
                    user_dev_release_notes = DevReleaseNotes('<ReleaseNotes></ReleaseNotes>', user_master_release_notes)
                    print(f'{dir.name.replace(".git", "")} has no user-release-notes.xml in master or dev') 

                main_module = MainModule(module_name, master_release_notes, dev_release_notes, user_master_release_notes, user_dev_release_notes)

                """
                Get the submodules for the Mainmodule
                """
                infrastructure = json.loads(Path('infrastructure.json').read_text())
                for repo_clone_link in infrastructure['subrepositories']:
                    _repo_name = repo_clone_link.split('/simplic/')[1]
                    _dir = Path(f'../../dev/build/clones/{_repo_name}')
                    
                    if _dir.exists():
                        if Path(f'{dir}/release-notes.xml').exists():
                            master_release_notes_xml = Path(f'{_dir}/release-notes.xml').read_text()

                            remote_repo = org.get_repo(_dir.name.replace('.git', ''))
                            try:
                                dev_release_notes_xml = remote_repo.get_contents('release-notes.xml', ref='dev').decoded_content
                            except GithubException:
                                dev_release_notes_xml = '<ReleaseNotes></ReleaseNotes>'
                                print(f'Submodule {_dir.name.replace(".git", "")} has no release-notes.xml in dev') 
                            
                                master_release_notes = MasterReleaseNotes(master_release_notes_xml)
                                dev_release_notes = DevReleaseNotes(dev_release_notes_xml, master_release_notes)
                            
                            solution_name = next(Path(_dir).rglob('*.sln')).name
                            module_name = solution_name.strip('.sln').replace('-', ' ').capitalize()
                            sub_module = SubModule(module_name, master_release_notes, dev_release_notes)
                            main_module.submodules.append(sub_module)
                    else:
                        print(f'{repo_name} was not yet added to the api documentation clone list and thus wont appear in release notes')

                main_modules.append(main_module)
    
    main_modules.sort(key=lambda x: x.name)

    """
    Generate Markdown
    """
    os.mkdir('../dev/')
    os.mkdir('../user/')
    
    for module in main_modules:
        try:
            print(f'Writing Release Notes for module {module}')
            write_release_notes(module, ReleaseNoteType.Dev)
            write_release_notes(module, ReleaseNoteType.User)
        except Exception as e:
            print(str(e))
    try:
        write_latest_release_notes(main_modules, ReleaseNoteType.User)
        write_latest_release_notes(main_modules, ReleaseNoteType.Dev)
    except Exception as e:
        print(str(e))

    write_toc(ReleaseNoteType.User)
    write_toc(ReleaseNoteType.Dev)