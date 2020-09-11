# Working with SqlExecute

In this code sample we will show how to execute sql commands.
## Required Modules

- [simplic.Sql](xref:RefTest)
  

## Samples

# [C#](#tab/tabcsharp)

```csharp

```

# [Python](#tab/tabpython)

```python
from System import Console
from simplic import Sql
res = Sql.execute("select * from it_contacts where CompanyName=?","default",["Thomson GmbH"])
for contact in res:
	Console.WriteLine(contact.FriendlyName)
```
***

## Expected Output
```
Thomson GmbH | Marco Belt
GKM Werbeagentur GmbH | Fr. Bartoschek
Wöhlk GmbH & Co. KG | Standort Dresden
```
