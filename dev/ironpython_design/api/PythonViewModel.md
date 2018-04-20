PythonViewModel
===

Python viewmodel


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.PythonViewModel.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import PythonViewModel

# usage
PythonViewModel.METHOD(...)
```


## Properties

## Methods

### CustomPropertyGetter
Will be called when a custom property getter is called

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the property | |
 | value | Value to return | |
 | propertyInfo | Property information object (might be null) | |

__Returns:__
Value to return for the property

### CustomPropertySetter
Will be called when a custom property setter is called

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the property | |
 | inValue | Value that should be set | |
 | outValue | Setted value | |
 | propertyInfo | Property information object (might be null) | |

__Returns:__
True when the value should be set, else false

### on_get
Will be called when a property getter is called

| Name | Summary |    |
| --- | --- | ---- |
 | property_name | Name of the property | |
 | value | Value to return | |
 | property_info | Property information object (might be null) | |

__Returns:__
Value to return for the property

### on_set
Will be called when a custom property setter is called

| Name | Summary |    |
| --- | --- | ---- |
 | property_name | Name of the property | |
 | value | Value that should be set | |
 | property_info | Property information object (might be null) | |

__Returns:__
Returns a value that should be set or a tuple, containing the True or False (whether to continue setting or not) and the value that should be set

### add_property
Add a property of a specific type to the list of properties

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the property | |
 | type | Property type | |

### add_property
Add a new property to the list of custom properties (Type = String)

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the custom property | |

### get_custom_property
Gets the value of a custom property

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the property | |

__Returns:__
Returns the value of the property if found, else null

### set_custom_property
Ads the value for a custom property

| Name | Summary |    |
| --- | --- | ---- |
 | name | Name of the property | |
 | value | Property value | |
