ReportManager
===

Module for working with EPL-Report within in the simplic framework


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.ReportManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import ReportManager

# usage
ReportManager.METHOD(...)
```


## Properties

## Methods

### print_report
Print a report by it's unique report-name, with optional parameter passing. Works only with report parameter

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |
 | printer | Simplic printer name. If no printer is passed, the default printer will be used | |
 | parameter | Optional parameter, dictioanry string:object (default python) | |

### get_configuration
Get simplic report configuration by it's unique name

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |

__Returns:__
Instance of a simplic report configuration

### get_report
Get an instance of a simplic report by it's unique, intern name

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |
 | parameter | Optional parameter, dictioanry string:object (default python) | |

__Returns:__
Return report instance if found

### get_report_pdf
Render report as pdf and return the pdf as byte-array

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |
 | parameter | Optional parameter, dictioanry string:object (default python) | |

__Returns:__
Byte-array containing the report as pdf

### get_report_tiff
Render report as tiff and return the tiff as byte-array

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |
 | parameter | Optional parameter, dictioanry string:object (default python) | |

__Returns:__
Byte-array containing the report as tiff
