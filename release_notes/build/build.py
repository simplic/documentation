import json
from github import Github, GithubException
from itertools import groupby
import os
from pathlib import Path
import lxml.etree as ET
from enum import Enum
import argparse
import string

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
        self.change_sets = [ChangeSet(_change_set) for _change_set in root if _change_set.get('date')]
        self.change_sets.sort(key=lambda x: (int(x.date.split('-')[0]), int(x.date.split('-')[1]), int(x.date.split('-')[2])), reverse=True)

    def get_latest_version_number(self):
        if self.change_sets:
            return self.change_sets[0].version
        else:
            return None

    def get_latest_date(self):
        if self.change_sets:
            return self.change_sets[0].date
        else:
            return None  

    def get_latest_change_sets(self):
        return self.get_change_sets_with_version(self.get_latest_version_number())
        
    def get_latest_change_sets_date(self):
        return self.get_change_sets_with_date(self.get_latest_date())

    def get_change_sets_with_version(self, version):
        return [change_set for change_set in self.change_sets if change_set.version == version]

    def get_change_sets_with_date(self, date):
        return [change_set for change_set in self.change_sets if change_set.date == date]

class DevReleaseNotes:
    def __init__(self, xml, master_release_notes):
        
        self.upcoming_change_sets = []
        
        if not xml:
            self.change_sets = []
            return
        
        root = ET.fromstring(xml)
        self.change_sets = [ChangeSet(_change_set) for _change_set in root]
        
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
        
        if _change.text:
            self.text = _change.text.strip()

class ReleaseNoteType(Enum):
    User = 1
    Support = 2
    Dev = 3

def write_latest_release_notes(main_modules, release_note_type):
   
    # User Release Notes Latest Changes
    if release_note_type == ReleaseNoteType.User:
        # open and append in the markdown file (if not existing, create md file)
        with open('../user/index.md', 'a+') as f:
            write_line(f, '# Latest Changes')

            for main_module in main_modules:
                # gets every latest change from a main module
                latest_change_sets = main_module.user_master_release_notes.get_latest_change_sets_date()

                # if there is something in the list    
                if latest_change_sets:

                    write_line(f, f'## [{main_module.name.title()}]({main_module.name.title().replace(" ", "%20")}.md)')
                    latest_change_set = aggregated_change_sets(latest_change_sets)[0]
                    write_line(f, latest_change_set.to_markdown(ReleaseNoteType.User, True))
                    write_line(f, '---')

            write_line(f, '# Upcoming Changes')
            
            for main_module in main_modules:
                upcoming_change_sets = main_module.user_dev_release_notes.upcoming_change_sets

                if upcoming_change_sets:
                    write_line(f, f'## [{main_module.name.title().replace}]({main_module.name.title().replace(" ", "%20")}.md)')
                    upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]
                    write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.User, False))
                    write_line(f, '---')

    # Dev Release Notes Latest Changes
    elif release_note_type == ReleaseNoteType.Dev:
        with open('../dev/index.md', 'a+') as f:
            write_line(f, '# Latest Changes')

            # sort the main_modules list by the date

            main_module_dict = {}
            main_module_list = []

            # sort
            for main_module in main_modules:

                # get the latest date of the release note
                latest_date = main_module.master_release_notes.get_latest_date()
                # Get the latest change set (latest date)
                latest_change_sets = main_module.master_release_notes.get_latest_change_sets_date()
               
                # add the main module name as a value and the date as a key in a dictionary
                main_module_dict[latest_date] = main_module
                       
            dict2={}    

            for x in main_module_dict.keys():
                if x != None:
                    dict2[x]=main_module_dict[x]

            main_module_dict = dict2
            dict2 = {}       

            for key in sorted(main_module_dict.keys(), reverse = True):
                dict2[key]=main_module_dict[key]

            # Put everything back in the main_modules list

            values = dict2.values()
            main_module_list = list(values)

            main_modules = main_module_list
                     
            for main_module in main_modules:
                latest_date = main_module.master_release_notes.get_latest_date()
                latest_change_sets = main_module.master_release_notes.get_latest_change_sets_date()

                if latest_change_sets or any([submodule.master_release_notes.get_change_sets_with_date(latest_date) for submodule in main_module.submodules]):
                    write_line(f, f'## [{main_module.name.title()}]({main_module.name.title().replace(" ", "%20")}/1main.md)')

                    if latest_change_sets:
                        latest_change_set = aggregated_change_sets_date(latest_change_sets)[0]
                        write_line(f, latest_change_set.to_markdown(ReleaseNoteType.Dev, True))
                
                    write_line(f, '---')

                for submodule in main_module.submodules:
                    change_sets_with_date = submodule.master_release_notes.get_change_sets_with_date(latest_date)

                    if change_sets_with_date:
                        write_line(f, f'#### [{submodule.name}]({main_module.name.title().replace(" ", "%20")}/{submodule.name.title().replace(" ", "%20")}.md)')
                        change_set = aggregated_change_sets_date(change_sets_with_date)[0]
                        
                        write_line(f, change_set.to_markdown(ReleaseNoteType.Dev, False))
                        write_line(f, '---')
            
            write_line(f, '# Upcoming Changes')
            for main_module in main_modules:
                upcoming_change_sets = main_module.dev_release_notes.upcoming_change_sets

                if upcoming_change_sets or any([submodule.dev_release_notes.upcoming_change_sets for submodule in main_module.submodules]):
                    write_line(f, f'## [{main_module.name.title()}]({main_module.name.title().replace(" ", "%20")}/1main.md)')

                    if upcoming_change_sets:
                        upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]
                        write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.Dev, False))
                
                    write_line(f, '---')

                for submodule in main_module.submodules:
                    upcoming_change_sets = submodule.dev_release_notes.upcoming_change_sets

                    if upcoming_change_sets:
                        write_line(f, f'#### [{submodule.name}]({main_module.name.title().replace(" ", "%20")}/{submodule.name.title().replace(" ", "%20")}.md)')
                        upcoming_change_set = aggregated_change_sets(upcoming_change_sets)[0]

                        write_line(f, upcoming_change_set.to_markdown(ReleaseNoteType.Dev, False))
                        write_line(f, '---')


def write_release_notes(main_module, release_note_type):
    if release_note_type == ReleaseNoteType.User:
        try:
            os.remove('../user/{main_module.name.title()}.md')
        except:
            print("")
        with open(f'../user/{main_module.name.title()}.md', 'a+') as f:
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
            with open(f'{dir_path}/{submodule.name.title()}.md', 'a+') as _f:
                write_line(_f, '# Release Notes')

                change_sets = submodule.master_release_notes.change_sets

                for change_set in aggregated_change_sets(change_sets):
                    write_line(_f, change_set.to_markdown(ReleaseNoteType.Dev, True))
                    write_line(_f, '---')

def write_line(file, string):
    file.write(f'{string}\n')

def aggregated_change_sets(unaggregated_change_sets):
    return [sum(list(change_set_group)) for _, change_set_group in groupby(unaggregated_change_sets, key=lambda x: x.version)]

def aggregated_change_sets_date(unaggregated_change_sets):
    return [sum(list(change_set_group)) for _, change_set_group in groupby(unaggregated_change_sets, key=lambda x: x.date)]    

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
    parser.add_argument('--git-token', help='Your GitHub password')
    args = vars(parser.parse_args())

    git_token = args['git_token']

    if not git_token:
        print('Enter all Arguments. Get a list of the arguments by adding --help to the script call. e.g. python build.py --help')
        exit()

    g = Github(git_token)
    org = g.get_organization('simplic')
    
    main_modules = []
    os.remove("../../support/error_codes.md")
    with open("../../support/error_codes.md", "a+") as e:
        introductionString = """
# Error codes \n
This page contains all error codes. Errors are separated into two parts: \n
* Message (Contains the error message) 
* Solution (Contains a possible solution for the error) \n
All error codes are separated by modules and have a unique error code. \n
## Error messages and codes 
    """
        write_line(e,introductionString)
    e.close()


    # read_text() returns the decoded contents of the pointed-to file as a string
    main_repositories = json.loads(Path('main_repositories.json').read_text())

    # split the string to get the name of the repository and the Path where it will be cloned from, happens for every repository in the "main_repositories.json"
    for link in main_repositories['links']:
        repo_name = link.split('/simplic/')[1]
        dir = Path(f'../../dev/build/clones/{repo_name}')

        print(dir, dir.exists())
        # If the Path exists:
        if dir.exists():
            # documentation_config.json -> string
            # infrastructure.json -> string  (in the infrastructure.json the subrepositories are mentioned)
            documentation_config = json.loads(Path(f'{dir}/documentation_config.json').read_text())
            infrastructure = json.loads(Path(f'{dir}/infrastructure.json').read_text())

            print(infrastructure)

            # the name of the module is what is written after 'part_of' as long it's not "core". If it's "core" the module name is Simplic Studio 
            module_name = documentation_config['part_of'] if documentation_config['part_of'] != 'core' else 'Simplic Studio'
            
            # if the repository has a release-notes.xml file it will be converted to string
            if Path(f'{dir}/release-notes.xml').exists():
                master_release_notes_xml = Path(f'{dir}/release-notes.xml').read_text()

                remote_repo = org.get_repo(dir.name.replace('.git', ''))
                try:
                    # xml to string from branch dev
                    dev_release_notes_xml = remote_repo.get_contents('release-notes.xml', ref='dev').decoded_content
                except GithubException:
                    # the release_notes.xml is empty
                    dev_release_notes_xml = '<ReleaseNotes></ReleaseNotes>'
                    print(f'{dir.name.replace(".git", "")} has no release-notes.xml in dev') 
           
                # release notes are imported from the release notes and sorted by date 
                master_release_notes = MasterReleaseNotes(master_release_notes_xml)
                dev_release_notes = DevReleaseNotes(dev_release_notes_xml, master_release_notes)

                try:
                    user_master_release_notes_xml = Path(f'{dir}/user-release-notes.xml').read_text()
                    user_dev_release_notes_xml = remote_repo.get_contents('user-release-notes.xml', ref='dev').decoded_content
                    user_master_release_notes = MasterReleaseNotes(user_master_release_notes_xml)
                    user_dev_release_notes = DevReleaseNotes(user_dev_release_notes_xml, user_master_release_notes)
                except Exception as e:
                    print(str(e))
                    user_master_release_notes = MasterReleaseNotes('<ReleaseNotes></ReleaseNotes>')
                    user_dev_release_notes = DevReleaseNotes('<ReleaseNotes></ReleaseNotes>', user_master_release_notes)
                    print(f'{dir.name.replace(".git", "")} has no user-release-notes.xml in master or dev') 

                main_module = MainModule(module_name, master_release_notes, dev_release_notes, user_master_release_notes, user_dev_release_notes)
                main_modules.append(main_module)

        	# ERROR CODES

            with open("../../support/error_codes.md", "a+") as e:
                write_line(e, '## '+dir.name.replace('.git', ''))
                if Path(f'{dir}/error_codes.xml').exists():
                    error_codes_xml = Path(f'{dir}/error_codes.xml').read_text()

                    remote_repo_error_codes = org.get_repo(dir.name.replace('.git', ''))
                    print(f'there are error codes in {dir}')

                    #write_line(e, '## '+dir.name.replace('.git', ''))

                    # First row of the table (the column titles)
                    write_line(e, "Error code|Error text|Message|Solution \n -|-|-|-")
                    tree = ET.fromstring(error_codes_xml)

                    localization_link = tree.attrib['Localization']
                    localization_link = localization_link.replace('.*.json', '.en-US.json')
                    # Throw exception if file not found...
                    try:
                        localization = json.loads(Path(f'{dir}/{localization_link}').read_text())
                    except:
                        print("Localization file couldn't be found")

                    for node in tree:
                        error_code = node.attrib['Code']
                        error_text = node.text.strip()
                        error_message = error_code+"_msg"
                        error_solution = error_code+"_sln"
                        try:
                            write_line(e, f'{error_code} |{error_text}|{localization[error_message]}|{localization[error_solution]}')
                        except:
                            write_line(e, f'{error_code} |{error_text}|not found|not found')
                else:
                    write_line(e, '{errors\\}')  
                     
                """
                Get the submodules for the Mainmodule
                """
            for repo_clone_link in infrastructure['subrepositories']:
                _repo_name = repo_clone_link.split('/simplic/')[1]
                _dir = Path(f'../../dev/build/clones/{_repo_name}')
                
                if _dir.exists():
                    if Path(f'{_dir}/release-notes.xml').exists():
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
                        module_name = string.capwords(solution_name.replace('.sln', ' ').replace('-', ' ').replace('.', ' '))
                        sub_module = SubModule(module_name, master_release_notes, dev_release_notes)
                        main_module.submodules.append(sub_module)

                    # ERROR CODES 
                    with open("../../support/error_codes.md", "a+") as e:                        
                        write_line(e, '### '+_dir.name.replace('.git', ''))
                        if Path(f'{_dir}/error_codes.xml').exists():
                            error_codes_xml = Path(f'{_dir}/error_codes.xml').read_text()
                            print(f'there are error codes in {_dir}')
                            remote_repo = org.get_repo(_dir.name.replace('.git', ''))

                        
                            

                            # First row of the table (the column titles)
                            write_line(e, "Error code|Error text|Message|Solution \n -|-|-|-")
                            tree = ET.fromstring(error_codes_xml)

                            localization_link = tree.attrib['Localization']
                            localization_link = localization_link.replace('.*.json', '.en-US.json')
                            # Throw exception if file not found...
                            try:
                                localization = json.loads(Path(f'{dir}/{localization_link}').read_text())
                            except:
                                print("Localization file couldn't be found")

                            for node in tree:
                                error_code = node.attrib['Code']
                                error_text = node.text.strip()
                                error_message = error_code+"_msg"
                                error_solution = error_code+"_sln"
                                try:
                                    write_line(e, f'{error_code} |{error_text}|{localization[error_message]}|{localization[error_solution]}')
                                except:
                                    write_line(e, f'{error_code} |{error_text}|not found|not found')
                        else:
                            write_line(e, '{errors\\}')  
                else:
                    print(f'{repo_name} was not yet added to the api documentation clone list and thus wont appear in release notes')
    
    main_modules.sort(key=lambda x: x.name)
    print(main_modules)
    """
    Generate Markdown
    """
    if not Path('../dev/').exists():
        os.mkdir('../dev/')
    if not Path('../user/').exists():
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
