# Addings SQLObjects to the Database API Documentation

You can add an SQLObject (Table, View, Procedure, ...) to the documentation by adding a comment (remark) to it.
This is most easily done directly inside SQLCentral.
The Comment has to be a rootless xml tree of structure

```xml
<module>Module</module>
<description>Sample description</description>
<deprecated>
    <description>
    This SQLObject is deprecated since 03 09 2020.
    </description>
    <name>Use instead Table Name</name>
    <module>Module of the Table to be used instead</module>
</deprecated>
```

### Comment tag explanation

Required

- **module**: The module the SQLObject belongs to (is used by).
- **description**: A description as to what the table is used for and the information it holds.

Optional

- **deprecated**: Only use this tag if the SQLObject is deprecated.
  - **description**: This is required if the SQLObject is deprecated. Use it to say since when the Object is deprecated or why etc.
  - **name**: This is optional and should be used to refer to a use instead alternative to the deprecated Object, incase it exists. Put the name of the alternative here.
  - **module**: This is optional and should be used to refer to a use instead alternative to the deprecated Object, incase it exists. Put the module of the alternative here.
