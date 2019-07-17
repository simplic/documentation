# Attribute - RequiredFieldInfo

This custom attribute contains the required fields to use the tagged function in a grid menu.
These fields must be returned from the grids sql.

```csharp
 [RequiredFieldInfo("(Name of the function)", new[] { "(tablename.fieldname)", "..." })]
```