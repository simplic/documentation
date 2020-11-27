# Working with updating a mail address and a phone number of a contact

In this code sample we will show how to update a mail address and a phone number of a contact.

## Required Modules

- [Simplic.PlugIn.SAC.Contact](xref:Simplic.PlugIn.SAC.Contact)
  - [Contact](xref:Simplic.PlugIn.SAC.Contact.Contact)
  - [ContactManager](xref:Simplic.PlugIn.SAC.Contact.ContactManager)
  - [PhoneNumber](xref:Simplic.PlugIn.SAC.Contact.PhoneNumber)
  - [EMailAddress](xref:Simplic.PlugIn.SAC.Contact.EMailAddress)
- [System](xref:System)
  - [Guid](xref:System.Guid)

## Samples


# Python

```python
from Simplic.PlugIn.SAC.Contact import Contact, ContactManager, PhoneNumber, EMailAddress
from System import Guid

# Create an instance of ContactManager
contact_manager = ContactManager()
# Get/Import a contact with the Guid
contact = contact_manager.Get(Guid.Parse("a1ba332c-8c8f-4e9f-9f5a-f5642ad6cfe5"))

# Update the phone number with the Id = 1
for phoneNumber in contact.PrimaryPhysicalAddress.LoadPhoneNumbers().GetItems():
	if phoneNumber.PhoneNumberKeyId == 1:
		phoneNumber.Number = "051213888887" 
		
# Update the E-Mail-Address with the Id = 0
for mailaddress in contact.PrimaryPhysicalAddress.LoadEMailAddresses().GetItems():
	if mailaddress.EMailAddressKeyId== 0:
		mailaddress.MailAddress= "maxmustermann@test.com" 	
		
# Save the changed contact
contact_manager.Save(contact)
```
***

## Expected Output
```
There is no output but the phone number an E-Mail-Address of the selected contact has changed. 
```