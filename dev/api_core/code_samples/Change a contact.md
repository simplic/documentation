# Working with changing a contact in Simplic

In this code sample we will show how to change a contact in Simplic.

## Required Modules

- [Simplic.PlugIn.SAC.Contact](xref:Simplic.PlugIn.SAC.Contact)
  - [Contact](xref:Simplic.PlugIn.SAC.Contact.Contact)
  - [ContactManager](xref:Simplic.PlugIn.SAC.Contact.ContactManager)
- [System](xref:System)
  - [Guid](xref:System.Guid)


## Samples

# Python

```python
from Simplic.PlugIn.SAC.Contact import Contact, ContactManager
from System import Guid
# Create an instance of Contact and ContactManager
contact = Contact()
contact_manager = ContactManager()
# Get/Import a contact with the Guid
contact = contact_manager.Get(Guid.Parse("a1ba332c-8c8f-4e9f-9f5a-f5642ad6cfe5"))
# Change p.ex. the first name
contact.FirstName = "Fred"
# Save the changed contact
contact_manager.Save(contact)
```
***

## Expected Output
```
No output but a contact has changed.
```
