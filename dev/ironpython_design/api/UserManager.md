UserManager
===

Module for working with simplic users


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.UserManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import UserManager

# usage
UserManager.METHOD(...)
```


## Properties

## Methods

### get_current_userid
Get current logged in user id

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
User id from the loggedin user

### get_current_username
Get current logged in username as string

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Username from the loggedin user

### get_current_friendlyusername
Get the friendly name from the current user. If not set it returns the user name

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Friendly user name (firstname  lastname), if not set it returns the current user name

### get_friendlyusername
Get the friendly username by a specific user id

| Name | Summary |    |
| --- | --- | ---- |
 | id | User id from which friendly name should be returned | |

__Returns:__
Friendly user name (firstname  lastname), if not set it returns the current user name

### get_firendlyusername
Get the friendly username by a specific user id

| Name | Summary |    |
| --- | --- | ---- |
 | id | User id from which friendly name should be returned | |

__Returns:__
Friendly user name (firstname  lastname), if not set it returns the current user name
