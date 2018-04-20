Sql
===

Python SQL-Module, for executing sql statement in the sybase sql anywhere database


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.Sql.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import Sql

# usage
Sql.METHOD(...)
```


## Properties

## Methods

### execute_none_query
Execute a query which has no result.

| Name | Summary |    |
| --- | --- | ---- |
 | query | Query to execute | |
 | conName | Connection-string or connection name, default connection name is 'default' | |
 | parameter | List of parameter which will be passed to the query | |

__Returns:__
Amount of affected entries

### execute
Execute a query with result (E.g. select statement)

| Name | Summary |    |
| --- | --- | ---- |
 | query | Query to execute | |
 | conName | Connection-string or connection name, default connection name is 'default' | |
 | parameter | List of parameter which will be passed to the query | |

__Returns:__
List of objects which represents the result. Every entry in the list represents a row, which contains an object with all columns

### execute_iter
Execute a query with result (E.g. select statement) and gives the result as enuerable

| Name | Summary |    |
| --- | --- | ---- |
 | query | Query to execute | |
 | conName | Connection-string or connection name, default connection name is 'default' | |
 | parameter | List of parameter which will be passed to the query | |

__Returns:__
Enumerable of objects which represents the result. Every entry in the enumerable represents a row, which contains an object with all columns
