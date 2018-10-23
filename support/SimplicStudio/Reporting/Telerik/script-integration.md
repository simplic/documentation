# Script integration

Simplic provides a few simple methods to print a report using python.

Printing a report:

```python
from simplic import ReportManager

# Print report
# The last parameter is a dictionary of key-values.
# The report must be of type parameter report
ReportManager.print_report('<report name>', 'printer name, or None for default', None)
```

## Print report as pdf

It is also possible to print a report directly as pdf and return it as a byte-array:

```python
from simplic import ReportManager

# The last parameter is a dictionary of key-values.
# The report must be of type parameter report
byte_array = ReportManager.get_report_pdf('<report name>', None)
```