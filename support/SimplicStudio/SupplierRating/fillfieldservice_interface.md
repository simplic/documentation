# IFillFieldValueService

You can create a custom service to automatically fill the fields of a new supplierrating.
After creating you service you need to select it from the combobox in the fielddefinition.
Services should be registered in the main.py file!

Below you can see a simple implementation of a service which implements the IFillFieldValueService.

# Example
This example uses the rating.ContactId to get the full contact and fill the fields StringValue with the companyname.

```python
from simplic import DependencyInjection, Sql

from Simplic.SupplierEvaluation import IFillFieldValueService
from Simplic.PlugIn.SAC.Contact import ContactManager

class SampleFillService(IFillFieldValueService):

    def get_ServiceName(self):
        return 'SampleFillService'

    def get_DisplayName(self):
        return 'SampleFillService'
        
    def FillFieldValue(self, rating, entry, field):
        manager = ContactManager()
        contact = manager.GetById(rating.ContactId)

        field.StringValue = contact.CompanyName
        return True    

DependencyInjection.register_instance(IFillFieldValueService, 'SampleFillService', SampleFillService())
```
