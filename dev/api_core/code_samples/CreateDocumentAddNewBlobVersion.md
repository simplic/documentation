# Working with creating documents and adding a new blob version.

In this code sample we will show how to create a document, add a new blob version and release it.
## Required Modules

- simplic
    - [ArchiveManager](xref:ArchiveManager)
    - [DependencyInjection](xref:DependencyInjection)
    - [StackRegisterHelper](xref:StackRegisterHelper)
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

# read/import a sample file
blob = File.ReadAllBytes('C:\\Users\\petersen\\Documents\\beispielDatei.txt')
# saves a blob in the archive system
id = ArchiveManager.set_blob(blob)
# create a sample document, give it a name and an extension
SampleDocument = Document()
SampleDocument.FileName = 'SampleDocument'
SampleDocument.FileExtension = '.txt'

# create new document version 
versionDoc = DocumentVersion()
# set the BlobGuid to id
versionDoc.BlobGuid = id
# add a version comment
versionDoc.VersionComment = 'V1'
# add version to document
SampleDocument.AddVersion(versionDoc)
# get a document service
service = DependencyInjection.resolve(IDocumentService)
# save the document
service.Save(SampleDocument)
# refresh the register
StackRegisterHelper.refresh_register('STACK_Document', SampleDocument.Guid)

# load document
existing_Sampledoc = service.GetById(SampleDocument.Guid)
# create new document version 
versionDoc = DocumentVersion()
# set the BlobGuid to id
versionDoc.BlobGuid = id
# add a version comment
versionDoc.VersionComment = 'V2'
# add version to document
existing_Sampledoc.AddVersion(versionDoc)
# release the version
existing_Sampledoc.ReleaseVersion(versionDoc)
# save the document
service.Save(existing_Sampledoc)
```
***

## Expected Output 
```
True

# You can see the new document and the two versions in the document manager.
```