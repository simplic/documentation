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
        # Pfad aus dem InPin Data01 einlesen
        file_path = scope.GetValue[str](self.node.InPinData01)

        # Aufbereitung Dateiname, C:\dev\demo\test.txt --> test.txt
        file_name = Path.GetFileNameWithoutExtension(file_path)
        extension = Path.GetExtension(file_path)

        # Ausgabe der Daten über den Scope
        scope.SetValue(self.node.OutPinData01, file_name)
        scope.SetValue(self.node.OutPinData02, extension)
```
***

## Required Methods and Parameters
```python
# Konstruktor mit dem Parameter "node"
def __init__(self, node):
# Execute mit den Parametern "runtime" und "scope"
def execute(self, runtime, scope):

```
