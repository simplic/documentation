ArchiveManager
===

Module for working with the simplic archive system, for getting and setting blobs


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.ArchiveManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import ArchiveManager

# usage
ArchiveManager.METHOD(...)
```


## Properties

## Methods

### set_blob
Save a blob in the archive system

| Name | Summary |    |
| --- | --- | ---- |
 | blob | Byte-array which contains the blob | |

__Returns:__
Id of the stored blob (guid)

### get_blob
Get a blob from the archive system

| Name | Summary |    |
| --- | --- | ---- |
 | id | Id of the blob | |

__Returns:__
Blob as byte-array if found

### archive_file
Archive a file with opening the coresponding document management ui. Mostly the one of the simplic application collection

| Name | Summary |    |
| --- | --- | ---- |
 | path | Path to the file to archvie | |
 | stack_name | Name of the stack, to connect instance data with | |
 | instance_data_ids | Instance datas which will be connected to the new created document | |
