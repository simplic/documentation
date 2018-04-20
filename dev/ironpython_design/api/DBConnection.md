DBConnection
===

Module for working with simplic connection strings


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.DBConnection.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import DBConnection

# usage
DBConnection.METHOD(...)
```


## Properties

## Methods

### user_default
Get the current default connection with user credentials

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Connection string with username and password

### get_by_name
Get connection string by it's name

| Name | Summary |    |
| --- | --- | ---- |
 | name | Connection string name | |

__Returns:__
Conenction string with username and password

### get_by_id
Get connection string by it's unique id

| Name | Summary |    |
| --- | --- | ---- |
 | id | Connection string id | |

__Returns:__
Conenction string with username and password
