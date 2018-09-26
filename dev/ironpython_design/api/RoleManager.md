RoleManager
===

Module for working with the simplic role system


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.RoleManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import RoleManager

# usage
RoleManager.METHOD(...)
```


## Properties

## Methods

### get_by_name
Get a public api role instance by it's unique name

| Name | Summary |    |
| --- | --- | ---- |
 | role_name | Unique role name | |

__Returns:__
Role if found, else null

### get_by_id
Get a public api role instance by it's unique id

| Name | Summary |    |
| --- | --- | ---- |
 | id | Unique role id | |

__Returns:__
Role if found, else null

### create
Create new simplic role

| Name | Summary |    |
| --- | --- | ---- |
 | role | Instance of the public api role object | |

__Returns:__
Created role instance

### update
Update existing simplic role

| Name | Summary |    |
| --- | --- | ---- |
 | role | Instance of the public api role object | |

### delete
Delete existing simplic role

| Name | Summary |    |
| --- | --- | ---- |
 | role | Instance of the public api role object | |

### delete_by_id
Delete existing simplic role instance by it's unique id

| Name | Summary |    |
| --- | --- | ---- |
 | role_id | Unique role guid | |

### current_user_has_access
Proof whether the current logged in user has access to a role

| Name | Summary |    |
| --- | --- | ---- |
 | role_name | Unique, intern role name | |

__Returns:__
True if the user has access. If all users are on "Default", false will be returned

### current_user_has_access_default
Proof whether the current logged in user has access to a role, returns also true if all users/groups are on "Default"

| Name | Summary |    |
| --- | --- | ---- |
 | role_name | Unique, intern role name | |

__Returns:__
True if the user has access. If all users are on "Default", also true will be returned

### user_has_access
Proof whether a specific user has access to a role

| Name | Summary |    |
| --- | --- | ---- |
 | role_name | Unique, intern role name | |
 | user_id | Simplic user id | |

__Returns:__
True if the user has access. If all users are on "Default", false will be returned

### user_has_access_default
Proof whether a specific user has access to a role, returns also true if all users/groups are on "Default"

| Name | Summary |    |
| --- | --- | ---- |
 | role_name | Unique, intern role name | |
 | user_id | Simplic user id | |

__Returns:__
True if the user has access. If all users are on "Default", also true will be returned
