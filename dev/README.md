# Dev

The api documentation for the Core aswell as the plugins is built automatically using docfx.
Adding a repository to the api documentation is as easy as doing the following two steps.

1. Add a json file with name `documentation_config.json` and structure

```
{
 "is_main_repo": true,
 "part_of": "Simplic HR",
 "contains_py_api": false,
 "py_api_xml_name": ""
}
```

to the main directory of your repositories the master branch.

2. Add the repositories HTTPS clone link to the `repositories.json` file located in /Build

If the repository you want to add is a main repository, it should also contain a manually written `introduction.md` file that describes what functionalities the plugin provides.

### Documentation Config variables explanation

- **is_main_repo**: A boolean value indicating whether the repository is the main repository of a module or not.
- **part_of**: A String indicating which module the repository is part of.
- **contains_py_api**: A boolean value indicating whether the repository contains Python API
- **py_api_xml_name**: A String containing the name of the generated xml file containing, that is used for generating the Python api documentation.
