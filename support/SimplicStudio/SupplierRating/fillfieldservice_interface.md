# IFillFieldValueService

You can create a custom service to automatically fill the fields of a new supplierrating.
After creating you service you need to select it from the combobox in the fielddefinition.
Services should be registered in the main.py file!

Below you can see a simple implementation of a service which implements the IFillFieldValueService.

# Example

```python
from simplic import DependencyInjection, Sql


from Simplic.SupplierEvaluation import IFillFieldValueService


class SampleFillService(IFillFieldValueService):

    def get_ServiceName(self):
        return 'SampleFillService'


    def get_DisplayName(self):
        return 'SampleFillService'
        
    def FillFieldValue(self, field):
        user_id = Sql.execute('SELECT MAX(Ident) Id from ESS_MS_Intern_User')
    
        field.IntegerValue = user_id[0].Id
        return True    

DependencyInjection.register_instance(IFillFieldValueService, 'SampleFillService', SampleFillService())
```