BarcodeValidation
===

Module for validating barcodes using the barcodes which are registered in the barcode validation configuration


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.BarcodeValidation.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import BarcodeValidation

# usage
BarcodeValidation.METHOD(...)
```


## Properties

## Methods

### validate
Execute script code directly in the default scope

| Name | Summary |    |
| --- | --- | ---- |
 | barcode | Barcode as string to validate | |

__Returns:__
Barcode validationr esult else none

### clear_cache
Clear the cache which contains all barcode validation rules

| Name | Summary |    |
| --- | --- | ---- |
