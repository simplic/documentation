# Python hooks

Using a python hook, the behavior of the simplic transaction system can be adjusted.

## Implementing a python hook

A python hook is a unity service, that must be registered in `/private/main.py`. A transaction hook
is always a python class, that derives from: `ITransactionHook`:

```python
from Simplic.ERP.Core import ITransactionHook

class ERPHook(ITransactionHook):

	def Create(self, transaction):
		pass
		
	def AddItem(self, transaction, item):
		pass
		
	def RemoveItem(self, transaction, item):
		pass
		
	def Organize(self, transaction):
		pass
```

A basic transaction hook has to look like the snipping above. To activate a hook, it must be registered:

```python
from simplic import DependencyInjection

DependencyInjection.register_instance(ITransactionHook, "ERPHook1", ERPHook())
```
The hook system will be called if one of the following actions will be executed:

* New transaction object is created
* An item was added
* An item was removed
* The transaction values are calcuted

### Sample hooks

**Setting a default transaction number:**

```python
from Simplic.ERP.Core import ITransactionHook
from simplic import DependencyInjection

class ERPHook(ITransactionHook):

	def Create(self, transaction):
		transaction.Number = "999999x"
		
	def AddItem(self, transaction, item):
		pass
		
	def RemoveItem(self, transaction, item):
		pass
		
	def Organize(self, transaction):
		pass

DependencyInjection.register_instance(ITransactionHook, "ERPHook1", ERPHook())
```

**Setting the default quantity to 10:**

```python
from Simplic.ERP.Core import ITransactionHook
from simplic import DependencyInjection
from Simplic.Data import PreciseDecimal

class ERPHook(ITransactionHook):

	def Create(self, transaction):
		pass
		
	def AddItem(self, transaction, item):
		item.Quantity = PreciseDecimal(10)
		
	def RemoveItem(self, transaction, item):
		pass
		
	def Organize(self, transaction):
		pass

DependencyInjection.register_instance(ITransactionHook, "ERPHook1", ERPHook())
```

## Acivating a hook for application server

__not done yet__