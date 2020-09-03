# Adding projects to the API Documentation

The api documentation for all repositories is built automatically using docfx.\
Adding a repository to the api documentation is as easy as doing the following two steps:

1. Add a json file with name `documentation_config.json` and structure

```json
{
 "is_main_repo": false,
 "part_of": "Plugin Name",
 "contains_py_api": false,
 "py_api_xml_name": "",
 "exclude": []
}
```

to the root directory of your repositories master branch.

2. Add the repositories HTTPS clone link to the `repositories.json` file located in dev/Build

If the repository you want to add is a main repository, it should also contain a manually written `introduction.md` file that describes what functionalities the plugin provides.

### Documentation Config variables explanation

- **is_main_repo**: A boolean value, indicating whether the repository is the main repository of a module or not.
- **part_of**: A String value, indicating which module the repository is part of.
- **contains_py_api**: A boolean value, indicating whether the repository contains Python API.
- **py_api_xml_name**: A string value, containing the name of the xml file that is used for generating the Python api documentation.
- **exclude**: A list containing the paths to directories or files to be excluded from the documentation. For the paths file mapping formats refer to the [docfx documentation](https://dotnet.github.io/docfx/tutorial/docfx.exe_user_manual.html#4-supported-file-mapping-format).

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
* **module**: The module the SQLObject belongs to (is used by).
* **description**: A description as to what the table is used for and the information it holds.
* 
Optional
* **deprecated**: Only use this tag if the SQLObject is deprecated.
  * **deprecated** > *description*: This is required if the SQLObject is deprecated. Use it to say since when the Object is deprecated or why etc.
  * **deprecated** > name & **deprecated** > module: This is optional and should be used to refer to a use instead alternative to the deprecated Object, incase it exists. Put the Name of the alternative Object in *name* and the module in *module*.
