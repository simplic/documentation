Script
===

Module for dynamically working with scripts inside of scripts. Should not be used for imports!


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.Script.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import Script

# usage
Script.METHOD(...)
```


## Properties

## Methods

### execute_expression
Execute script code directly in the default scope

| Name | Summary |    |
| --- | --- | ---- |
 | expression | Code to execute | |

__Returns:__
None

### execute_script
Execute a script by it's name or path from the repository

| Name | Summary |    |
| --- | --- | ---- |
 | script_path | Path to the script | |
 | force_execution | True if execution should be forst, regardles if it was already executed or not | |

### create_class_instance
Create a class instance by passing the class name and a list of arguments for the constructor. The class/module must exists in the current scope.

| Name | Summary |    |
| --- | --- | ---- |
