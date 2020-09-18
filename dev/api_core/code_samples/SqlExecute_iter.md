# Working with SqlExecute

In this code sample we will show how to execute sql commands.
## Required Modules

- simplic
  - [simplic.Sql](xref:PythonAPI.Sql)
  

## Samples

# Python
```python
from System import Console
from simplic import Sql
# creates a dynamic list with all the selected columns and rows
res = Sql.execute("select FriendlyName from it_contacts where CompanyName='B. Kaufmann'")
Console.WriteLine(len(res))
for contact in res:
	# You can use this command to print the column (here: FriendlyName). The column has to be in the Select-Statement or it won't work.
	Console.WriteLine(contact.FriendlyName) 
```
***

## Expected Output with execute
```
100
Thomson GmbH | Marco Belt
GKM Werbeagentur GmbH | Fr. Bartoschek
Wöhlk GmbH & Co. KG | Standort Dresden
```
## Expected Output with execute_iter
```
Error message "object of type 'WhereSelectEnumerableIterator[ScriptSqlResult, object]' has no len()" because execute_iter returns an enumerable Iterator which has no length. 

The difference between execute and execute_iter is that execute returns a list and execute_iter an enumerable Iterator. It can only read the current line and return the next line without "knowing" what was in the row before.
```