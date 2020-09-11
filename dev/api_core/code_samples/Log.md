# Working with the logging system

In this code sample we will show how to write into the logging system. The system will automatically write the output to the database (`ESS_MS_Intern_Exception`) and the file-system `%localappdata%\Simplic\<section>\Log`. The default section is named `default`.
## Required Modules

- [System](xref:System) 
  - [Exception](xref:System.Exception)
- simplic  
  - [Log](xref:PythonAPI.Log)
  

## Samples

# Python

```python
from simplic import Log
from System import Exception
Log.info("message")

try:
	raise
except Exception as ex:
	Log.error("errormessage", ex)

# The debug output will only be executed for active debug-areas. To activate a debug
# area, the application argument --debug-area is required.
# Sample: ApplicationServer.exe --debug-area sample_area
# Sample: Simplic Studio.exe --debug-area sample_area
# Furthermore, the time between two debug-commands will be tracked and evaluated.
Log.debug("debug-message", "sample_area")
Log.warning("warning-message")
```
***

## Expected Output
```
Entries in the log:
p.ex. a message with the message "message" if it's just an information, "errormessage" if an error occured and "warning" if there's a warning. 
"debug" only works when debug-areas are enabled.
```
