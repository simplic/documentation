# Working with Python Flow Node Scripts

In this code sample we will show how to read and output data from the database with a Python Script in the FLow Node System.

## Required Modules

- [Simplic.Flow](xref:Simplic.Flow)
  - [DataPinScope](xref:Simplic.Flow.DataPinScope)
  - [IFlowRuntimeService](xref:Simplic.Flow.IFlowRuntimeService)
  - [ActionNode](xref:Simplic.Flow.ActionNode)
- simplic
  - [simplic.Sql](xref:PythonAPI.Sql)

## Samples

# Python

```python
from simplic import Sql

class PythonFlowNodeScript:

    def __init__(self, node):
        self.node = node

    def execute(self, runtime, scope):

        names = []
        res = Sql.execute("select UserName from ESS_MS_Intern_User")

        for ESS_MS_Intern_User in res:
            names.append(ESS_MS_Intern_User.UserName)

        scope.SetValue(self.node.OutPinData01, names)
        scope.SetValue(self.node.OutPinData02, res[0].UserName)
```

---

## Output

```
In this sample the output is a list of all usernames (OutPinData01) and after that the first object in the previous list (OutPinData02).
```
