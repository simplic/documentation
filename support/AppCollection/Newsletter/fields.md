# Variable newsletter fields

Variables can be used by typing the following placeholde in the newsletter html code.

| Template       | Value                               |
|----------------|-------------------------------------|
| {CustomerId}   | Customer id from IT_Contacts (Guid) |
| {NewsletterId} | Unique id of the newsletter         |
| {LicenseId}    | License id of the newsletter system |

Further more, all columns are available that are selected in the underlying grid.
A column can be used in the newsletter html code like this: `{<column-name-in-lower-case>}`.

For example:

![~/images/newsletter-columns.png](~/images/newsletter-columns.png)

Sample: `{companyname}`.
