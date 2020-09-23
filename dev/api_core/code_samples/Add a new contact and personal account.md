# Working with adding a contact and a personal account to Simplic

In this code sample we will show how to add a contact and a personal account to Simplic.

## Required Modules

- [Simplic.PlugIn.SAC.Contact](xref:Simplic.PlugIn.SAC.Contact)
  - [Contact](xref:Simplic.PlugIn.SAC.Contact.Contact)
  - [ContactManager](xref:Simplic.PlugIn.SAC.Contact.ContactManager)
  - [PhysicalAddress](xref:Simplic.PlugIn.SAC.Contact.PhysicalAddress)
  - [PersonalAccountManager](xref:Simplic.PlugIn.SAC.Contact.PersonalAccountManager)
- [System](xref:System)
  - [Guid](xref:System.Guid)


## Samples


# Python

```python
from Simplic.PlugIn.SAC.Contact import Contact, ContactManager, PhysicalAddress, PersonalAccountManager
from System import Guid

# Create an instance of Contact
contact = Contact()
# Add a ContactTypeKeyId: 1 is a firm contact, 2 is a personal contact
contact.ContactTypeKeyId = 1
# Add some attributes like Company name, first name, last name, salutation, ...
contact.CompanyName = "Simplic GmbH"
contact.FirstName = "Max"
contact.LastName = "Mustermann"
contact.Salutation = "Herr"

# Create an instance of PhysicalAddress
physical_address = PhysicalAddress()
# Add some attributes like the City, Street, Zipcode, ...
physical_address.City = "Hildesheim"
physical_address.Street = "Hauptstraße 2"
physical_address.Zipcode = "31139"
physical_address.Country = "Deutschland"
physical_address.Country_Iso = "DE"
physical_address.District = "Stadt"
physical_address.PhysicalAddressKeyId = 0
# Add the address to the new contact
contact.PrimaryPhysicalAddress = address

# Create an instance of PersonalAccountManager
personal_account_manager = PersonalAccountManager()
# Get a sample personal account 
sample_personal_account = personal_account_manager.Get(Guid.Parse("764E2808-1243-45EC-B510-3E9F588A8817"))
# Create a new personal account from the sample account
personal_account = sample_personal_account.CreateFromSample()
# Add the new personal account to the new contact
contact.PersonalAccounts.Add(personal_account)
# Create an instance of ContactManager
contact_manager = ContactManager()
# Save the new contact
contact_manager.Save(contact)
```
***

## Expected Output
```
No output but a contact is added to contacts.
```
