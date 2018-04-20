PythonWindowHook
===

Window python hook


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.PythonWindowHook.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import PythonWindowHook

# usage
PythonWindowHook.METHOD(...)
```


## Properties

## Methods

### #ctor
Initialize new PythonWindowHook

| Name | Summary |    |
| --- | --- | ---- |
 | window_instance | Window instance | |

### OnOpenPage
Will be called before the page was opened

| Name | Summary |    |
| --- | --- | ---- |

### on_open_page
Will be called before the page was opened

| Name | Summary |    |
| --- | --- | ---- |

### PageOpened
Will be called when the data are opened

| Name | Summary |    |
| --- | --- | ---- |

### page_opened
Will be called when the data are opened

| Name | Summary |    |
| --- | --- | ---- |

### OnSave
Will be called when data are saved

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Returns true when data should be saved

### on_save
Will be called when data are saved

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Returns true when data should be saved

### Saved
Will be called after data are saved

| Name | Summary |    |
| --- | --- | ---- |

### saved
Will be called after data are saved

| Name | Summary |    |
| --- | --- | ---- |

### OnDelete
Will be called when deleteing data

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Returns whether to continue the delete process or not

### on_delete
Will be called when deleteing data

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Returns whether to continue the delete process or not

### Deleted
Will be called when the delete process finished

| Name | Summary |    |
| --- | --- | ---- |

### deleted
Will be called when the delete process finished

| Name | Summary |    |
| --- | --- | ---- |
