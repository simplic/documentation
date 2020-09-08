# Working with the logging system

In this code sample we will show how to write into the logging system.
## Required Modules

- [System](xref:System) 
  - [Exception](xref:System.Exception)
- [simplic](PythonAPI.simplic)  
  - [Log](PythonAPI.Log)
  

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

Log.debug("debug")
Log.warning("warning")
```
***

## Expected Output
```
Entries in the log:
p.ex. a message with the message "message" if it's just an information, "errormessage" if an error occured and "warning" if there's a warning. 
"debug" only works when debug-areas are enabled.
```
