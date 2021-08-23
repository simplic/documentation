# simplic-supplier-evaluation

Contains a simplic plugin for supplier evaluation management.

It consists of a main model, "SupplierRating" which can have multiple "SupplierratingEntry"s which again can have multiple "Field"s.
These fields are defined in "FieldDefinition"s.

The supplierrating references one contact and you can not have more than one supplierrating for each contact.

It is possible to create a service which derives from the "IFillFieldValueSerivce" interface to create logic that calculates an initiale value for a field.
If the service is register in the DI-container it will be displayed for selection in the fielddefinition-window.
