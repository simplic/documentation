# Working with printing and archiving a transaction

In this code sample we will show how to print and archive a transaction. 
## Required Modules

- [Simplic.ERP.Core](xref:Simplic.ERP.Core) 
  - [Archive.TransactionArchiveManager](xref:Simplic.ERP.Core.Archive.TransactionArchiveManager)
  - [TransactionManager](xref:Simplic.ERP.Core.TransactionManager)
- [simplic](PythonAPI.simplic)
    - [Sql](PythonAPI.Sql)
  

## Samples

# Python

```python
from simplic import Sql
from Simplic.ERP.Core import TransactionManager
from Simplic.ERP.Core.Archive import TransactionArchiveManager

a = TransactionArchiveManager()
m = TransactionManager()

for row in Sql.execute("select guid from IT_Transaction where TransactionDate = Convert(date, '01.09.2020', 104) and documentid is not null"):
	t = m.Get(row.Guid)
	t.LoadItems()
	
	a.Archive(t)
```
***

## Expected Output
```
```
