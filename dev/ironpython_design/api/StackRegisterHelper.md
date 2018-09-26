StackRegisterHelper
===

Module for working with simplic stacks and register.


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.StackRegisterHelper.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import StackRegisterHelper

# usage
StackRegisterHelper.METHOD(...)
```


## Properties

## Methods

### get_stack_name_by_guid
Get the name of a stack by it's id

| Name | Summary |    |
| --- | --- | ---- |
 | id | Unique id of the stack | |

__Returns:__
Name of the stack. Should start with STACK_

### get_stack_guid_by_name
Get the stack guid by it's name

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Unique name of the stack, should start with STACK_* | |

__Returns:__
Unique id of the stack

### get_stack_table
Get the stack-table-name by stack name

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Unique name of the stack, should start with STACK_* | |

__Returns:__
Table name as string

### is_stack_existing
Proof whether a stack exists.

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Unique name of the stack, should start with STACK_* | |

__Returns:__
Returns true, if the stack exists

### refresh_register
Refresh all register assignmets for an instance data entry

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Unique name of the stack, should start with STACK_* | |
 | instance_data_guid | Unique instance data guids | |

### get_assinged_register
Returns a list of register ids, in which an instance data is assigned to

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Unique name of the stack, should start with STACK_* | |
 | instance_data_guid | Instance data for proofing | |

__Returns:__
List of instance data guids

### connect
Connect an instance data entry with a list of target instance data entries

| Name | Summary |    |
| --- | --- | ---- |
 | source_stack_name | Unique name of the stack, should start with STACK_*. This stack is the source of the connection | |
 | source_guid | Instance data entry which which all targets will be connected | |
 | target_stack_name | Unique name of the stack, should start with STACK_*. This stack is the target of the connection | |
 | target_guids | Targets which will be connecteod with the source | |
 | is_twoway | If set to true (default), the connection between source and target will be in both ways, elso only from source to target | |

### remove_connection_list
Remove a list of instance data connection between source and target

| Name | Summary |    |
| --- | --- | ---- |
 | source_stack_name | Name of the source stack | |
 | source_guid | Id of the source instance data entry | |
 | target_stack_name | Name of the target stack | |
 | target_guids | List of ids (target entries) | |
 | is_twoway | If set to true, the connection will be removed in both directions | |

### remove_connection
Remove an instance data connection between source and target

| Name | Summary |    |
| --- | --- | ---- |
 | source_stack_name | Name of the source stack | |
 | source_guid | Id of the source instance data entry | |
 | target_stack_name | Name of the target stack | |
 | target_guid | Target instance data entry guid | |
 | is_twoway | If set to true, the connection will be removed in both directions | |

### has_connections
Returns true if the instance data has connections, false if it doesn't have any connections

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Stack name | |
 | instance_data_guid | Instancedata guid | |

__Returns:__
None

### has_connections
Returns true if the instance data has connections, false if it doesn't have any connections

| Name | Summary |    |
| --- | --- | ---- |
 | stack_guid | Stack name | |
 | instance_data_guid | Instancedata guid | |

__Returns:__
None
