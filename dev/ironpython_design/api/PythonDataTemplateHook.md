PythonDataTemplateHook
===

Python DataTemplate hook


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.PythonDataTemplateHook.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import PythonDataTemplateHook

# usage
PythonDataTemplateHook.METHOD(...)
```


## Properties

### content

Gets or sets the content of the data template

## Methods

### #ctor
Initialize new PythonDataTemplateHook

| Name | Summary |    |
| --- | --- | ---- |
 | content | Template instance | |

### load
Will be called when the data template was loaded

| Name | Summary |    |
| --- | --- | ---- |

### unload
Will be called when the datatemplate was unloaded

| Name | Summary |    |
| --- | --- | ---- |

### find_control
Find a control in the data template

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the control (x:Name) | |

__Returns:__
Returns an instance of the object
