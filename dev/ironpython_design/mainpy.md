# IronPython entrypoint (main.py)

The simplic framework (Simplic Studio) provides an entrypoint for IronPython scripting. The file
must be placed under `/private/main.py`. The file will be executed after the user login was successfull.

Sample:

```python
from simplic import Log

def init():
	Log.info('Entrypoint was called')

init()
```