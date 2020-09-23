# Working with changing a personal account in Simplic

In this code sample we will show how to change a personal account in Simplic.

## Required Modules

- [Simplic.PlugIn.SAC.Contact](xref:Simplic.PlugIn.SAC.Contact)
  - [PersonalAccountManager](xref:Simplic.PlugIn.SAC.Contact.PersonalAccountManager)
- [System](xref:System)
  - [Guid](xref:System.Guid)

## Samples


# Python

```python
from Simplic.PlugIn.SAC.Contact import PersonalAccountManager 
from System import Guid

# Create an instance and PersonalAccountManager
personal_account_manager = PersonalAccountManager()

# Get/Import a personal account with the Guid
personal_account = personal_account_manager.Get(Guid.Parse("a7fe9ffe-1495-43cd-a87d-ad2c45e8dc9a"))
# Change p.ex. if it's deleted or not
personal_account.IsDeleted = False
# Save the changed contact
personal_account_manager.Save(personal_account)
```
***

## Expected Output
```
No output but a personal account has changed.
```