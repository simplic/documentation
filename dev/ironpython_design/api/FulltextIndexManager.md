FulltextIndexManager
===

Module for working with the simplic fulltext index. For example adding task for processing fulltexts.


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.FulltextIndexManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import FulltextIndexManager

# usage
FulltextIndexManager.METHOD(...)
```


## Properties

## Methods

### add_instancedata_task
Add a task to generate the fulltext for an instance data

| Name | Summary |    |
| --- | --- | ---- |
 | stack_name | Name of the stack (intern) | |
 | instance_data_guid | Guid of the instance data | |

### add_document_task
Add task for processing the fulltext/document extraction from a document by it's blob_guid.

| Name | Summary |    |
| --- | --- | ---- |
 | blob_guid | Unique id of the blob (blob_guid) | |
 | file_extension | File extension for processing the content (.pdf, ...) | |
