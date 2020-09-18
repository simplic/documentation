from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from pathlib import Path
import re
from argparse import ArgumentParser
import git
from pathlib import Path
import re
import timeit
from enum import Enum
from azure.devops.v6_0.work_item_tracking.models import JsonPatchOperation
from azure.devops.v6_0.work_item_tracking.models import WorkItemRelation


class NewIssue:
    def __init__(self, repository_name):
        self.repository_name = repository_name

    def add_to_azure(self, parent_epic_url, work_item_tracking_client):
        """
        Adds an issue to azure as a child of the given epic
        """
        relation = WorkItemRelation(rel='System.LinkTypes.Hierarchy-Reverse', url=parent_epic_url)

        json_patch_document = [
            JsonPatchOperation(path='/fields/System.Title', op='add', value=self.repository_name),
            JsonPatchOperation(path='/relations/-', op='add', value=relation)
        ]
        work_item_tracking_client.create_work_item(json_patch_document, project='simplic-framework', type='Issue')

class ExistingIssue:
    def __init__(self, title, issue_id):
        self.issue_id = issue_id
        self.title = title
        self.code_todos = []

    def __repr__(self):
        return f'Title: {self.title}, Id: {self.issue_id}, CodeToDo\'s: {len(self.code_todos)}'


class NewCodeToDo:
    def __init__(self, repository_name, file_path, todo_text, description):
        self.repository_name = repository_name
        self.file_path = file_path
        self.todo_text = todo_text
        self.description = description

    def add_to_azure(self, parent_issue_url, work_item_tracking_client):
        """
        Adds itself to the azure boards as a child of the issue with id == issue_id
        """
        relation = WorkItemRelation(rel='System.LinkTypes.Hierarchy-Reverse', url=parent_issue_url)

        json_patch_document = [ 
            JsonPatchOperation(path='/fields/System.Title', op='add', value=self.todo_text[:150]),
            JsonPatchOperation(path='/fields/Custom.FilePath', op='add', value=self.file_path),
            JsonPatchOperation(path='/fields/Custom.ToDoText', op='add', value=self.todo_text),
            JsonPatchOperation(path='/fields/System.Description', op='add', value=f'<pre><code><div>{self.description}</div></code></pre>'),
            JsonPatchOperation(path='/relations/-', op='add', value=relation)
        ]
        work_item_tracking_client.create_work_item(json_patch_document, project='simplic-framework', type='CodeToDo')


class ExistingCodeToDo:
    def __init__(self, id, file_path, todo_text, state, parent_issue_name):
        self.id = id
        self.file_path = file_path
        self.todo_text = todo_text
        self.state = state
        self.parent_issue_name = parent_issue_name

    def still_exists(self):
        """
        Checks if an Exisiting ToDo is still found in the given file path
        """
        path = Path(self.file_path)
        
        # If file doesnt exist anymore or the todo isnt found in the file => Todo doesnt exists anymore
        if not path.exists() or (path.exists() and not re.search(fr'(?i)(todo:\s?)({re.escape(self.todo_text)})', path.read_text())):
            return False
        return True

    def set_state_on_azure(self, new_state, work_item_tracking_client):
        """
        Sets the state of itself on azure
        """
        json_patch_document = [JsonPatchOperation(path='/fields/System.State', op='replace', value=new_state.value)]
        
        if work_item_tracking_client.update_work_item(json_patch_document, self.id, project='simplic-framework'):
            print(f'The State of CodeToDo with Text: {self.todo_text.strip()} in {self.file_path} was set to {new_state.value}')
    
    def __repr__(self):
        return f'Id: {self.id}, FilePath: {self.file_path}, ToDoText: {self.todo_text}'


class CodeToDoState(Enum):
    To_do = "To do"
    Doing = "Doing"
    Not_found = "Not found"
    Done = "Done"

def get_issues(epic_id):
    """
    Returns the Child Issues of the given Epic
    """
    todo_epic = work_item_tracking_client.get_work_items([epic_id], project='simplic-framework', expand='Relations')[0]
    if not todo_epic.relations:
        return []
    else:
        issue_ids = [relation.url.split('/workItems/')[1] for relation in todo_epic.relations if relation.attributes['name'] == 'Child']
        issues = work_item_tracking_client.get_work_items(issue_ids, project='simplic-framework', expand='Relations')
        
        return issues


def get_existing_issues(epic_id):
    """
    Returns a List of ExistingIssue Objects, that are filled with their corresponding ExistingCodeToDo Objects
    """
    existing_issues = []

    for response in get_issues(epic_id):
        issue = ExistingIssue(response.fields['System.Title'], response.id)

        code_todo_ids = [relation.url.split('/workItems/')[1] for relation in response.relations if relation.attributes['name'] == 'Child']
    
        if code_todo_ids:
            code_todo_response = work_item_tracking_client.get_work_items(code_todo_ids, project='simplic-framework', fields=['Custom.FilePath', 'Custom.ToDoText', 'System.State'])
            
            existing_code_todos = []
            for response in code_todo_response:
                existing_code_todo = ExistingCodeToDo(response.id, response.fields['Custom.FilePath'], response.fields['Custom.ToDoText'], CodeToDoState(response.fields['System.State']), issue.title)
                existing_code_todos.append(existing_code_todo)

            issue.code_todos = existing_code_todos
        
        existing_issues.append(issue)

    return existing_issues

def verify_existing_code_todos(clone_path, existing_code_todos):
    """
    Verifies whether an existing CodeToDo is still in the code and sets the status of the CodeToDo accordingly.
    """
    if clone_path.exists():
        for code_todo in existing_code_todos:
            # if a code todo isnt found and its state is not already set to 'Not found' on azure
            if not code_todo.still_exists() and not code_todo.state == CodeToDoState.Not_found:
                code_todo.set_state_on_azure(CodeToDoState.Not_found, work_item_tracking_client)
            # if a previously not found todo that exists in azure is suddenly found again
            elif code_todo.still_exists() and code_todo.state == CodeToDoState.Not_found:
                code_todo.set_state_on_azure(CodeToDoState.To_do, work_item_tracking_client)
    else:  # Ignore if clone cant be found
        print(f'Couldent find clone dir @{clone_path}')


def get_new_code_todos(clone_dir, repository_name, existing_code_todos):
    new_code_todos = []

    for f in clone_dir.rglob('*.cs'):
        file_content = f.read_text(errors='ignore')

        found_todos = re.finditer(todo_regex, file_content)

        for todo in found_todos:
            if not todo_exists_already(f, todo.group(3), existing_code_todos):
                todo_text = todo.group(3)
                description = todo.group(0)
                new_code_todo = NewCodeToDo(repository_name, f, todo_text, description)
                new_code_todos.append(new_code_todo)

                print(f'New Todo Nr. {len(new_code_todos)} found in {f}')

    return new_code_todos

def todo_exists_already(new_file_path, new_todo_text, existing_code_todos):
    exists = False

    for existing_todo in existing_code_todos:
        if new_file_path == Path(existing_todo.file_path) and new_todo_text == existing_todo.todo_text:
            exists = True

    return exists


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--personal-access-token',
                        help='The personal access token.')
    args = vars(parser.parse_args())

    personal_access_token = args['personal_access_token']

    if not personal_access_token:
        exit()
    

    todo_regex = r'(?i)(.*\n){2}(.*todo:\s?)(.*\n)(.*\n){1,20}'

    organization_url = 'https://dev.azure.com/simplic-cloud'
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)
    work_item_tracking_client = connection.clients.get_work_item_tracking_client()

    epic_id = 545

    """
    Verify the existing code_todos by changing the state accordingly
    """
    existing_issues = get_existing_issues(epic_id)
    for issue in existing_issues:
        clone_path = Path(f'{issue.title}.git')
        verify_existing_code_todos(clone_path, issue.code_todos)


    """
    Look for todos in all cloned_dirs and save non existing ones
    """
    new_issues = []
    new_code_todos_all_dirs = [] # The new code todos for all dirs

    for dir in Path('.').iterdir(): # Execute from clones folder
        try:
            repo = git.Repo(dir)
            repo.git.checkout('dev')
        except git.exc.InvalidGitRepositoryError:
            print(f'Directory {dir} is not a Git repository => Skipping it.')
            continue
        except git.exc.GitCommandError:
            print(f'Couldent checkout dev branch of {dir} => Using active branch {repo.active_branch} (for now!)')
            continue


        repository_name = dir.name.replace('.git', '')

        if [issue.code_todos for issue in existing_issues if issue.title == repository_name]:
            existing_code_todos = [issue.code_todos for issue in existing_issues if issue.title == repository_name][0]
        else:
            existing_code_todos = []
            
        new_code_todos = get_new_code_todos(dir, repository_name, existing_code_todos)
        new_code_todos_all_dirs += new_code_todos
        
        if new_code_todos and not any([existing_issue for existing_issue in existing_issues if existing_issue.title == repository_name]):
            new_issue = NewIssue(repository_name)
            new_issues.append(new_issue)
    

    print(f'Found {len(new_issues)} new Issues and {len(new_code_todos_all_dirs)} new CodeToDo\'s')
    
    """
    Add the new issues to Azure
    """
    parent_epic_url = work_item_tracking_client.get_work_items([epic_id], project='simplic-framework')[0].url
    for issue in new_issues:
        issue.add_to_azure(parent_epic_url, work_item_tracking_client)


    """
    Add the new code_todos to azure
    """
    issues = get_issues(epic_id)

    for code_todo in new_code_todos_all_dirs:
        parent_issue = [issue for issue in issues if issue.fields['System.Title'] == code_todo.repository_name][0]
        code_todo.add_to_azure(parent_issue.url, work_item_tracking_client)