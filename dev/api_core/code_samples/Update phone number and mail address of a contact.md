# Working with updating a mail address and a phone number of a contact

In this code sample we will show how to change a mail address and a phone number of a contact.

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
from System import Guid, Console

# Create an instance of ContactManager
contact_manager = ContactManager()
# Get/Import a contact with the Guid
contact = contact_manager.Get(Guid.Parse("a1ba332c-8c8f-4e9f-9f5a-f5642ad6cfe5"))
# Create an instance of PhoneNumber
phone_number = PhoneNumber()
# Add a PhoneNumberKeyId
phone_number.PhoneNumberKeyId = 1
# Set a phone number
phone_number.Number = "05121344567" 
# Add a phone number to the contact
contact.PrimaryPhysicalAddress.PhoneNumbers.Add(phone_number)

# Update the phone number with the Id = 1
for phoneNumber in contact.PrimaryPhysicalAddress.PhoneNumbers.GetNewItems():
	if phoneNumber.PhoneNumberKeyId == 1:
		phone_number.Number = "051213888887" 
# Create an instance of EMailAddress	
mail_address = EMailAddress()
# Add a EMailAddressKeyId
mail_address.EMailAddressKeyId = 0
# Set an E-Mail-Address
mail_address.MailAddress = "mustermann@test.de"
# Add an E-Mail-Address to the contact
contact.PrimaryPhysicalAddress.EMailAddresses.Add(mail_address)

# Update the E-Mail-Address with the Id = 0
for mailaddress in contact.PrimaryPhysicalAddress.EMailAddresses.GetNewItems():
	if mailaddress.EMailAddressKeyId== 0:
		mail_address.MailAddress= "maxmustermann@test.com" 	
```
***

## Expected Output
```
There is no output but the phone number an E-Mail-Address of the selected contact has changed. 
```