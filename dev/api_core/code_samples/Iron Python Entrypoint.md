# Working with an IronPython entrypoint (main.py)

In this code sample we will show how to work with an IronPython entrypoint. The simplic framework (Simplic Studio) provides an entrypoint for IronPython scripting. The file must be placed under /private/main.py in the simplic repository. The file will be executed after the user login was successfull.
## Required Modules

- simplic
  - [Log](xref:PythonAPI.Log)

## Samples

# Python

```python
from simplic import Log

def init():
    # Writing a message in the Log
    Log.info('Entrypoint was called')

init()
```
***

## Expected Output
```
There will be an entry in the Log with the message "Entrypoint was called".
```
