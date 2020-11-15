# Working with setting user rights

In this code sample we will show how to set user rights in Simplic.

## Required Modules

- simplic
  - [DependencyInjection](xref:PythonAPI.DependenyInjection)
- [System](xref:System)
  - [Guid](xref:System.Guid)
- [Simplic.Authorization](xref:Simplic.Authorization)
  - [RowAccess](xref:Simplic.Authorization.RowAccess)
  - [IAuthorizationService](xref:Simplic.Authorization.IAuthorizationService)

## Samples


# Python

```python
from simplic import DependencyInjection
from System import Guid
from Simplic.Authorization import RowAccess, IAuthorizationService

class UserRights:


	def __init__(self, node):
		self.node = node

	def execute(self, runtime, scope):
        # Getting the path of the InPin Data01 out of the scope (a pin always belongs to a node).
        # Setting the expected type [Guid] and [int]
		document_id = scope.GetValue[Guid](self.node.InPinData01)
		user_id = scope.GetValue[int](self.node.InPinData02)
    
		# Setting the document access
		self.set_document_access(document_id, user_id)
    
	def set_document_access(self, document_id, user_id):
		# Getting the Authorization Service
		service = DependencyInjection.resolve(IAuthorizationService)
		# Getting the RowAccess of the given row id
		# First parameter (string): Table to query (IT_Document)
		# Second parameter (string): Name of the id column (Guid)
		# Third parameter (object): Actual rowId (document_id)
		access_obj = service.GetAccessRights('IT_Document', 'Guid', document_id)
		# Changing the OwnerId using the user_id
		access_obj.OwnerId = user_id

		# If the user doesn't have access to the row he gets full access 
		if user_id not in access_obj.UserFullAccess:
			access_obj.UserFullAccess.Add(user_id)

		# Setting the access rights for a given row in the given table	
		service.SetAccess('IT_Document', 'Guid', document_id, access_obj)
```
***

## Expected Output
```
There is no output but the user has full access now. 
```
