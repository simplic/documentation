# Working with changing document meta data in flow node

In this code sample we will show how to change document meta data in flow node.
## Required Modules

- [System.IO](xref:System.IO) 
  - [Path](xref:System.IO.Path)

## Samples

# Python

```python
from System.IO import Path

class DocumentTitleNode:

    def __init__(self, node):
        self.node = node

    def execute(self, runtime, scope):
        # Getting the path of the InPin Data01 out of the scope (a pin always belongs to a node).
        # Setting the expected type [str]
        file_path = scope.GetValue[str](self.node.InPinData01)

        # Rehashing the filename without the extension, C:\dev\demo\test.txt --> test.txt 
        file_name = Path.GetFileNameWithoutExtension(file_path)
        extension = Path.GetExtension(file_path)

        # Changing the PinData with the Scope
        scope.SetValue(self.node.OutPinData01, file_name)
        scope.SetValue(self.node.OutPinData02, extension)
```
***

## Required Methods and Parameters
```python
# Constructor with the parameter"node"
def __init__(self, node):
# Execute with the parameters "runtime" und "scope"
# runtime: execution of the flow system
# scope: the data is transferred within the scope
def execute(self, runtime, scope):
```
