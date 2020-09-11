import json
from github import Github
import xml.etree.ElementTree as ET
from itertools import groupby
import os
from pathlib import Path

# variables with underscores contain xml elements
class MainModule:
    def __init__(self, name, release_notes, dev_release_notes, user_release_notes, dev_user_release_notes):
        self.name = name
        self.release_notes = release_notes
        self.dev_release_notes = dev_release_notes
        self.user_release_notes = user_release_notes
        self.dev_user_release_notes = dev_user_release_notes

        self.submodules = []

class SubModule:
    def __init__(self, name, release_notes, dev_release_notes, user_release_notes, dev_user_release_notes):
        self.name = name
        self.release_notes = release_notes
        self.dev_release_notes = dev_release_notes
        self.user_release_notes = user_release_notes
        self.dev_user_release_notes = dev_user_release_notes

class ChangeSet:
    def __init__(self, _change_set):  # version,
        self.version = _change_set.get('version')
        self.date = _change_set.get('date')

        self.changes = [Change(_change) for _change in _change_set]

    def is_upcoming(self):
        return self.version is None

    def to_markdown(self):
        markdown = ''
        if (self.version and self.date):
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
            markdown += '**Enhancements**\n'
            for enhancement in enhancements:
                markdown += f'* {enhancement.text}\n'

        if bug_fixes:
            markdown += '**Bug fixes**\n'
            for bug_fix in bug_fixes:
                markdown += f'* {bug_fix.text}\n'

        return markdown

    def to_markdown_user(self):
        pass

    # Aggregate multiple xml _change_sets in to one with this
    def __add__(self, other):
        if self.version == other.version:
            self.changes += other.changes
            return self
        else:
            print('Couldent aggregate change sets.')

    def __radd__(self, other):
        if not other:
            return self
        else:
            return self.__add__(other)

    def __len__(self):
        return len(self.changes)

class Change:
    def __init__(self, _change):
        self.type = _change.get('type')
        self.text = _change.text

class ReleaseNotes:
    def __init__(self, xml):
        root = ET.fromstring(xml)

        unaggregated_change_sets = [ChangeSet(_change_set) for _change_set in root]

        # Aggregate change_sets with same version number
        self.change_sets = [sum(list(change_set_group)) for _, change_set_group in groupby(unaggregated_change_sets, key=lambda x: x.version)]

    def get_latest_version_number(self):
        version_numbers = [change_set.version.split('.') for change_set in self.change_sets if change_set.version]
        latest_major_number = sorted(version_numbers, key=lambda x: (x[0], x[1], x[2][:-2]), reverse=True)[0]

        return '.'.join(latest_major_number)

    def get_latest_change_set(self):
        latest_version_number = self.get_latest_version_number()
        latest_change_set = [change_set for change_set in self.change_sets if change_set.version == latest_version_number][0]

        return latest_change_set

    def get_upcoming_change_set(self):
        upcoming_change_set = [change_set for change_set in self.change_sets if change_set.is_upcoming()][0]

        return upcoming_change_set

    def get_ordered_change_sets(self):
        change_sets_with_version = [change_set for change_set in self.change_sets if not change_set.is_upcoming()]
        ordered_change_sets = sorted(change_sets_with_version,
                                         key=lambda x: (x.version.split('.')[0], x.version.split('.')[1], x.version.split('.')[2][:-2]),
                                         reverse=True
                                     )

        return ordered_change_sets # self.get_upcoming_change_sets() Hier brauchen wir ja die upcoming nicht

def write_line(file, string):
    file.write(f'{string}\n')

def write_index(main_modules, dev):
    index_path = f'../dev/index.md' if dev else f'../user/index.md'
    with open(index_path, 'a+') as f:
        # Latest changes
        write_line(f, f'# Latest Changes')
        for main_module in main_modules:
            if dev:
                latest_change_set = main_module.release_notes.get_latest_change_set()
                full_file_path = f'../dev/{main_module.name}.md'
            else:
                latest_change_set = main_module.user_release_notes.get_latest_change_set()
                full_file_path = f'../user/{main_module.name}.md'

            if len(latest_change_set):
                write_line(f, f'## [{main_module.name}]({full_file_path})')
                write_line(f, latest_change_set.to_markdown())
                write_line(f, '---')

            for submodule in main_module.submodules:
                if dev:
                    latest_change_set = submodule.release_notes.get_latest_change_set()
                else:
                    latest_change_set = submodule.user_release_notes.get_latest_change_set()

                if len(latest_change_set):
                    write_line(f, f'#### [{submodule.name}]({submodule.name}.md)') # TODO: Sollen die submodules ueberhaupt eigene files bekommen?
                    write_line(f, latest_change_set.to_markdown())
                    write_line(f, '---')

        # Upcoming changes. TODO: Types sind hier patch. Sollten auch bug etc. sein
        write_line(f, f'# Upcoming Changes')
        for main_module in main_modules:
            if dev:
                upcoming_change_set = main_module.dev_release_notes.get_upcoming_change_set()
                full_file_path = f'../dev/{main_module.name}.md'
            else:
                upcoming_change_set = main_module.dev_user_release_notes.get_upcoming_change_set()
                full_file_path = f'../user/{main_module.name}.md'


            if len(upcoming_change_set):
                write_line(f, f'## [{main_module.name}]({full_file_path})')
                write_line(f, upcoming_change_set.to_markdown())
                write_line(f, '---')

            for submodule in main_module.submodules:
                if dev:
                    upcoming_change_set = submodule.dev_user_release_notes.get_latest_change_set()
                else:
                    upcoming_change_set = submodule.dev_user_release_notes.get_latest_change_set()

                if len(upcoming_change_set):
                    write_line(f, f'#### [{submodule.name}]({submodule.name}.md)') # TODO: Sollen die submodules ueberhaupt eigene files bekommen?
                    write_line(f, upcoming_change_set.to_markdown())
                    write_line(f, '---')

def write_release_notes(main_module, dev):
    file_path = f'../dev/{main_module.name}.md' if dev else f'../user/{main_module.name}.md'
    with open(file_path, 'a+') as f:
        write_line(f, '# Release Notes')
        if dev:
            ordered_change_sets = main_module.release_notes.get_ordered_change_sets()
        else:
            ordered_change_sets = main_module.user_release_notes.get_ordered_change_sets()

        for change_set in ordered_change_sets:
            write_line(f, change_set.to_markdown())
            write_line(f, '---')

def write_toc(dir):
    with open(f'{dir}/toc.yml', 'w+') as f:
        toc = ''.join([f'- name: {f[:-3]}\n  href: {f}\n' for f in os.listdir('../dev') if f.endswith('.md')])
        f.write(toc)

# parser = argparse.ArgumentParser()
# parser.add_argument('--git-user', help='Your GitHub username')
# parser.add_argument('--git-pass', help='Your GitHub password')
# args = vars(parser.parse_args())
#
# git_user = args['git_user']
# git_pass = args['git_pass']
#
# if not git_user or not git_pass:
#     print('Enter all Arguments. Get a list of the arguments by adding --help to the script call. e.g. python build.py --help')
#     exit()

#g = Github(git_user, git_pass)
# org = g.get_organization('simplic')

main_modules = []

for dir in Path('../../dev/build/clones/').iterdir():
    submodules = []
    documentation_config = json.loads(Path(f'{dir}/documentation_config.json').read_text())

    if Path(f'{dir}/release-notes.xml').exists():
        with open(f'{dir}/release-notes.xml', 'r') as f:
            # remote_repo = org.get_repo(dir.name.replace(".git", ""))
            # dev_release_notes_xml = remote_repo.get_contents('release-notes.xml', 'heads/dev').decoded_content
            # user_dev_release_notes_xml = remote_repo.get_contents('user-release-notes.xml', 'heads/dev').decoded_content
            dev_release_notes_xml = Path('dev-test-release-notes.xml').read_text()
            user_release_notes_xml = Path('test-user-release-notes.xml').read_text() # Path(f'../../dev/build/clones/{dir.name}/user-release-notes.xml')
            dev_user_release_notes_xml = Path('dev-test-user-release-notes.xml').read_text()

            release_notes = ReleaseNotes(f.read())
            dev_release_notes = ReleaseNotes(dev_release_notes_xml)
            user_release_notes = ReleaseNotes(user_release_notes_xml)
            dev_user_release_notes = ReleaseNotes(dev_user_release_notes_xml)

            if documentation_config['is_main_repo']:
                module = MainModule(documentation_config['part_of'], release_notes, dev_release_notes, user_release_notes_xml, dev_user_release_notes)
                main_modules.append(module)
            else:
                module = SubModule(documentation_config['part_of'], release_notes, dev_release_notes, user_release_notes_xml, dev_user_release_notes)
                submodules.append(module)

    [mm.submodules.append(sm) for sm in submodules for mm in main_modules if sm.part_of == mm.name]

# Full markdown generation
# os.mkdir('../dev/')
# os.mkdir('../user/')
write_index(main_modules, dev=True)
write_index(main_modules, dev=False)

for main_module in main_modules:
    write_release_notes(main_module, dev=True)
    write_release_notes(main_module, dev=False)

write_toc('../dev/')
write_toc('../user/')






