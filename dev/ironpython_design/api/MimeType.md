MimeType
===

The MimeType module provides functions to work with a large set of mime types


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.MimeType.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import MimeType

# usage
MimeType.METHOD(...)
```


## Properties

## Methods

### get_mimetype
Get mime type from extension

| Name | Summary |    |
| --- | --- | ---- |
 | extension | Extension with or without dot | |

__Returns:__
Mime-type if found, else null

### get_extension
Get extension by mime type with dot

| Name | Summary |    |
| --- | --- | ---- |
 | mime_type | Mime type as string | |

__Returns:__
Extension as string with dot

### get_extension_no_dot
Get extension by mime type without dot

| Name | Summary |    |
| --- | --- | ---- |
 | mime_type | Mime type as string | |

__Returns:__
Extension as string without dot
