Role
===

Module for working with the simplic role system


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.Role.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import Role

# usage
Role.METHOD(...)
```


## Properties

### role_id

Get/Set unique role id

### display_name

Get/Set display name of the role

### intern_name

Get/Set internname of the role

### export_id

Get/Set export id, only used for dcef packages

### description

Get/Set description of the role

## Methods

### #ctor
Create a new empty role instance

| Name | Summary |    |
| --- | --- | ---- |

### #ctor
Create from ef role

| Name | Summary |    |
| --- | --- | ---- |
 | role | Role instance | |

### GetAsEFRole
Return as entity framework role

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
EF role
