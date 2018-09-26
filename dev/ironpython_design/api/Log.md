Log
===

Python module for writing to the simplic log system (Database, File-System, Console).


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.Log.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import Log

# usage
Log.METHOD(...)
```


## Properties

## Methods

### info
Write information to the logging system.

| Name | Summary |    |
| --- | --- | ---- |
 | message | Message text | |

### debug
Write debug information to the logging system. Will only be used, when the debug area is enabled.
            Debug-areas must be enabled over the simplic studio arguments: debug-area 'area-name'

| Name | Summary |    |
| --- | --- | ---- |
 | message | Message text | |
 | debug_area | Debug-area which will be used for filtering | |

### warning
Write warning to the simplic logging system

| Name | Summary |    |
| --- | --- | ---- |
 | message | Message text | |

### error
Write an error message to the logging system

| Name | Summary |    |
| --- | --- | ---- |
 | message | Message text | |
 | exception | Exception instance if exists, else None | |
