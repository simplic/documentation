# Working with creating documents and adding a new blob version.

In this code sample we will show how to create a document, add a new blob version and release it.
## Required Modules

- simplic
    - [ArchiveManager](xref:PythonAPI.ArchiveManager)
    - [DependencyInjection](xref:PythonAPI.DependencyInjection)
    - [StackRegisterHelper](xref:PythonAPI.StackRegisterHelper)
- [Simplic.Document](xref:Simplic.Document)
  - [Document](xref:Simplic.Document.Document)
  - [DocumentVersion](xref:Simplic.Document.DocumentVersion)
  - [IDocumentService](xref:Simplic.Document.IDocumentService)
- [System.IO](xref:System.IO)
  - [File](xref:Syste,.IO.File)
  

## Samples

# Python

```python
from simplic import ArchiveManager, DependencyInjection, StackRegisterHelper
from Simplic.Document import Document, DocumentVersion, IDocumentService
from System.IO import File

# Read/Import a sample file
blob = File.ReadAllBytes('C:\\Users\\petersen\\Documents\\beispielDatei.txt')
# Save a blob in the archive system
id = ArchiveManager.set_blob(blob)
# Create a sample document, give it a name and an extension
SampleDocument = Document()
SampleDocument.FileName = 'SampleDocument'
SampleDocument.FileExtension = '.txt'

# Create new document version 
versionDoc = DocumentVersion()
# Set the BlobGuid to id
versionDoc.BlobGuid = id
# Add a version comment
versionDoc.VersionComment = 'V1'
# Add version to document
SampleDocument.AddVersion(versionDoc)
# Get a document service
service = DependencyInjection.resolve(IDocumentService)
# Save the document
service.Save(SampleDocument)
# Refresh the register
StackRegisterHelper.refresh_register('STACK_Document', SampleDocument.Guid)

# Load document
existing_Sampledoc = service.GetById(SampleDocument.Guid)
# Create new document version 
versionDoc = DocumentVersion()
# Set the BlobGuid to id
versionDoc.BlobGuid = id
# Add a version comment
versionDoc.VersionComment = 'V2'
# Add version to document
existing_Sampledoc.AddVersion(versionDoc)
# Release the version
existing_Sampledoc.ReleaseVersion(versionDoc)
# Save the document
service.Save(existing_Sampledoc)
```
***

## Expected Output 
```
True

# You can see the new document and the two versions in the document manager.
```