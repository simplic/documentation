# Working with Setting and Removing User Rights

In this code sample we will show how to set and remove User Rights. 

## Required Modules

- simplic
  - [DependencyInjection](xref:PythonAPI.DependenyInjection)
- [Simplic.Authorization](xref:Simplic.Authorization)
  - [RowAccess](xref:Simplic.Authorization.RowAccess)
  - [IAuthorizationService](xref:Simplic.Authorization.IAuthorizationService)

## Sample


# Python

### Setting user rights
```python
# Import
from simplic import DependencyInjection
from Simplic.Authorization import RowAccess, IAuthorizationService

	def set_document_access(self, document_id):
        # Getting the Authorization Service
		service = DependencyInjection.resolve(IAuthorizationService)
		# Sample groupId's
        user_group_1 = 7
		accounting = 10
        # Getting the Access of the given document_id
        # First parameter (string): Table to query (IT_Document)
		# Second parameter (string): Name of the id column (Guid)
		# Third parameter (object): Actual rowId (document_id)
		access_obj = service.GetAccessRights('IT_Document', 'Guid', document_id)

        # Selecting a column with sql
		for access in Sql.execute('select UserGroupId from p_IT_Document_Workflow WHERE DocumentId = ? and UserGroupId != 0', 'Default', [document_id]):
            # If the UserGroup with the UserGroupId doesn't have access, the UserGroup will be added to the group with full access
			if access.UserGroupId not in access_obj.GroupFullAccess:
				access_obj.GroupFullAccess.Add(access.UserGroupId)
        # If the group with the GroupId=7 doesn't have full access, the GroupId will be added to the full access group and now the user_group_1 has full access, too
		if user_group_1 not in access_obj.GroupFullAccess:
			access_obj.GroupFullAccess.Add(user_group_1)
		# The same as above but with another GroupId	
		if accounting not in access_obj.GroupFullAccess:
			access_obj.GroupFullAccess.Add(accounting)

		# Sets the access rights
		service.SetAccess('IT_Document', 'Guid', document_id, access_obj)
```
***
### Removing User Rights
```python
# Import
from simplic import DependencyInjection
from Simplic.Authorization import RowAccess, IAuthorizationService

	def set_document_access(self, document_id):

		service = DependencyInjection.resolve(IAuthorizationService)
        user_group_1 = 7
		accounting = 10
		access_obj = service.GetAccessRights('IT_Document', 'Guid', document_id)

       	for access in Sql.execute('select UserGroupId from p_IT_Document_Workflow WHERE DocumentId = ? and UserGroupId != 0', 'Default', [document_id]):
            # If the UserGroup has access, it will be removed from the Group with full access
			if access.UserGroupId in access_obj.GroupFullAccess:
				access_obj.GroupFullAccess.Remove(access.UserGroupId)
        # If the group with the GroupId=7 has full access, the GroupId will be removed from the full access group and now the user_group_1 doesn't have full access anymore
		if user_group_1 in access_obj.GroupFullAccess:
			access_obj.GroupFullAccess.Remove(user_group_1)
		# The same as above but with another GroupId	
		if accounting in access_obj.GroupFullAccess:
			access_obj.GroupFullAccess.Remove(accounting)

		# Resets the access rights
		service.ResetAccess('IT_Document', 'Guid', document_id, access_obj)
```
***
## Expected Output
```
There is no output but access is added or removed. 
```