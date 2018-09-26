PythonTableViewModel
===

Python viewmodel


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.PythonTableViewModel.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import PythonTableViewModel

# usage
PythonTableViewModel.METHOD(...)
```


## Properties

### use_delete

Gets or sets whether data should be deleted. Default is false

### table_name

Gets the table name

### scheme

Gets the table schmene. Default is 'admin'

## Methods

### create
Initialize the viewmodel and fill its content

| Name | Summary |    |
| --- | --- | ---- |

### load
Load the data

| Name | Summary |    |
| --- | --- | ---- |
 | primary_keys | primary key | |

### save
Save addon values

| Name | Summary |    |
| --- | --- | ---- |

### delete
Delete addon values, only if

| Name | Summary |    |
| --- | --- | ---- |
