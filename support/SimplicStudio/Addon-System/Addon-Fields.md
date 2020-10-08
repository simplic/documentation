Addon-Fields
===

In order to display and store customer-specific information for instance data records, it is possible to use add-on fields.

## Configuration

To add addon fields to a record, a table must be created in the Simplic database. The table
must start with the name of the instance data table and additionally an `_Addon` must be appended. 

For example:

1. IT_Contacts -> **IT_Contacts_Addon**
2. IT_Document -> **IT_Document_Addon**


The addon table must contain a column with the name `Guid` (datatype: `Uniqueidentifier`) which is used to link the addon record to an instance record.
All other columns, as long as they have a comment, can be maintained via the UI. The comment (`remark`)
to a column, is used as display text in the user interface. For an addon table the following data types are allowed:


1. `Varchar` -> for text
2. `Integer`/`BigInt` -> for whole numbers
3. `Date` -> Für date
4. `DateTime` -> for date and time
5. `Numeric`/`Double` -> for floating point number

If an instance data table is stored for a file, the Simplic framework takes care of the display on the user interface.