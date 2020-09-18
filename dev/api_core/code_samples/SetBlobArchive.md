# Working with setting a blob from the archive

In this code sample we will show how to set a blob from the archive.
## Required Modules

- simplic
    - [ArchiveManager](xref:ArchiveManager)

## Samples

# Python

```python
from simplic import ArchiveManager
from System.IO import File

# read/import a sample file
blob = File.ReadAllBytes('C:\\Users\\petersen\\Documents\\beispielDatei.txt')
# saves a blob in the archive system
id = ArchiveManager.set_blob(blob)
```
***

## Expected Output 
```
```