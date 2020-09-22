# Working with constant and dynamic parameters to insert or update a table in sql

In this code sample we will show how to insert and update a table in sql with constant and dynamic parameters.
## Required Modules

- simplic
  - [simplic.Sql](xref:PythonAPI.Sql)
  

## Samples

# Python

```python
from simplic import Sql

# name as a dynamic parameter 
name = "Lutz"
# NameId as a dynamic parameter
NameId = "3"

# Inserting a constant parameter ("Igor") to a table (testInsertUpdate) in the column "Name"
res = Sql.execute_none_query("insert into testInsertUpdate (Name) values (?)", "default", ["Igor"])
# Inserting the dynamic parameter name to a table in the column "Name"
res = Sql.execute_none_query("insert into testInsertUpdate (Name) values (?)", "default", [name])
# Replacing a name in the given row (constant parameter = 2) with the parameter name.
res = Sql.execute_none_query("update testInsertUpdate set Name = ? where ID = ?", "default", [name, 2])
# Replacing a name in a specific row (dynamic parameter NameId) with the parameter name.
res = Sql.execute_none_query("update testInsertUpdate set Name = ? where ID = ?", "default", [name, NameID])
```
***

## Expected Output 
```
Two new entries at the end of the column "Name".
The second and third name changes to "Lutz".
```