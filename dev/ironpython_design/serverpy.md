# IronPython entrypoint (server.py)

The simplic framework (Application Server) provides an entrypoint for IronPython scripting (server-side). The file
must be placed under `/private/server.py` in the __simplic repository__. The script will be executed when all application server modules
are loaded.

Sample:

```python
from simplic import Log

def init():
	Log.info('Entrypoint was called')

init()
```

> Important: The script should not contain any UI-code! Furthermore, all not-ui code that is executed in the main.py should be executed in the server.py as well!