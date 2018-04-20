SequenceManager
===

Module for working with sequences, e.g. generate new sequence numbers.


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.SequenceManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import SequenceManager

# usage
SequenceManager.METHOD(...)
```


## Properties

## Methods

### generate
Generate a new number with the given sequence number by it's name

| Name | Summary |    |
| --- | --- | ---- |
 | sequence_name | Name of the sequence (intern name) | |
 | date | DateTime, if null is passed, the current DateTime will be used (DateTime.Now) | |

__Returns:__
Generated number
