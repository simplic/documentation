# Dev

The api documentation for all repositories is built automatically using docfx.\
Adding a repository to the api documentation is as easy as doing the following two steps:

1. Add a json file with name `documentation_config.json` and structure

```
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
