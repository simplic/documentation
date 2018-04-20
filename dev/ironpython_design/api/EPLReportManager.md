EPLReportManager
===

Module for working with EPL-Report within in the simplic framework


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.EPLReportManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import EPLReportManager

# usage
EPLReportManager.METHOD(...)
```


## Properties

## Methods

### print_report
Print an epl by it's unique report-name, with optional parameter passing

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |
 | printer | Simplic printer name. If no printer is passed, the default printer will be used | |
 | parameter | Optional parameter, dictioanry string:object (default python) | |

### get
Get epl report instance by it's unique name

| Name | Summary |    |
| --- | --- | ---- |
 | report_name | Name of the report (intern name) | |

__Returns:__
Instance of a simplic epl report
