WorkflowManager
===

Module for working with the simplic workflow system


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.WorkflowManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import WorkflowManager

# usage
WorkflowManager.METHOD(...)
```


## Properties

## Methods

### push_to_workflow
Push a list of instance data to a specific workflow

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | stack_name | Unique, internname of the stack | |
 | instance_data_guids | List of instance data gudis | |

__Returns:__
Result of the push process

### push_to_step
Push a list of instance data to a specific workflow step

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | step_name | Unique, internname of the workflow | |
 | stack_name | Unique, internname of the stack | |
 | instance_data_guids | List of instance data gudis | |

__Returns:__
Result of the push process

### push_to_next_step
Push a list of instance datas to the next available steps

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | stack_name | Unique, internname of the stack | |
 | instance_data_guids | List of instance data gudis | |

__Returns:__
Result of the push process

### is_in_workflow
Proof whether a specific instance data is in a workflow

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | instance_data_guid | Instance data guid | |

__Returns:__
True if the instance data is in the specific workflow

### is_in_workflow_step
Proof whether a specific instance data is in a workflow step

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | step_name | Unique, internname of the workflow | |
 | instance_data_guid | Instance data guid | |

__Returns:__
True if the instance data is in the specific workflow step

### get_current_workflow_step
Get the workflow step an instance data item is currently in within a specifiied workflow

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) to check | |
 | instance_data_guid | Instance data guid | |

__Returns:__
The internal name of the workflow step the instance data item is currently in, None if the item is not in any step within that workflow

### remove_from_workflow
Remove a list of instance datas from a specific workflow (all steps)

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | stack_name | Unique, internname of the stack | |
 | instance_data_guids | List of instance data gudis | |

### remove_from_workflow_step
Remove a list of instance datas from a specific workflow step

| Name | Summary |    |
| --- | --- | ---- |
 | workflow_name | Intern name of the workflow (unique name) | |
 | step_name | Unique, internname of the workflow | |
 | stack_name | Unique, internname of the stack | |
 | instance_data_guids | List of instance data gudis | |

__Returns:__
Result of the remove process
