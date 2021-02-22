# IronPython entrypoint (main.py)

The simplic framework (Simplic Studio) provides an entrypoint for IronPython scripting. The file
must be placed under `/private/main.py` in the __simplic repository__. The file will be executed after the user login was successfull.

Sample:

```python
from simplic import Log

def init():
	Log.info('Entrypoint was called')

init()
```

> All not-ui code that is executed in the main.py should be executed in the server.py as well!