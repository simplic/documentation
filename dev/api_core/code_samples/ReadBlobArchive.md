# Working with reading a blob from the archive

In this code sample we will show how to read a blob from the archive.
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
# get the blob from the id
sample = ArchiveManager.get_blob(id)

```
***

## Expected Output 
```
```