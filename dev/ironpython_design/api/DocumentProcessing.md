DocumentProcessing
===

Module for working with documents like pdfs or tiffs. E.g. you can convert documents.


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.DocumentProcessing.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import DocumentProcessing

# usage
DocumentProcessing.METHOD(...)
```


## Properties

## Methods

### pdf_to_tiff
Convert a pdf to tiff document

| Name | Summary |    |
| --- | --- | ---- |
 | pdf | Pdf which should be converted | |

__Returns:__
Instance of a byte-array which contains the converted document

### tiff_to_pdf
Convert a tiff to pdf document

| Name | Summary |    |
| --- | --- | ---- |
 | tiff | Tiff which should be converted | |

__Returns:__
Instance of a byte-array which contains the converted document

### get_mail_content
Gets the mail body from msg as byte array

| Name | Summary |    |
| --- | --- | ---- |
 | msg | Message as byte-array | |

__Returns:__
Maul body as string

### get_mail_rtf_content
Gets the mail body from msg as byte array

| Name | Summary |    |
| --- | --- | ---- |
 | msg | Message as byte-array | |

__Returns:__
Maul body as string

### get_mail_content_from_file
Gets the mail body from msg file

| Name | Summary |    |
| --- | --- | ---- |
 | path | Path to msg file | |

__Returns:__
Mail body as string

### get_mail_rtf_content_from_file
Gets the mail body from msg file

| Name | Summary |    |
| --- | --- | ---- |
 | path | Path to msg file | |

__Returns:__
Mail body as string

### get_mail_attachments
Gets a list of mail attachments

| Name | Summary |    |
| --- | --- | ---- |
 | msg | Mail message as byte-array | |

__Returns:__
List of tuples (string, byte[])

### get_mail_attachments_from_file
Gets a list of mail attachments

| Name | Summary |    |
| --- | --- | ---- |
 | path | Path to a mail nessage | |

__Returns:__
List of tuples (string, byte[])
