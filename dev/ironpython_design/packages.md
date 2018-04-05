# Packages within the simplic repository

The simplic IronPython integration supports packages within the simplic repository. If `__init__.py` files are placed in a directory,
it will be recognized as package.

A structure could look like this:

```
\/__init__.py
\/packages_sample\/__init__.py
\/packages_sample\/PackageSample.py
```


__PackageSample.py__

```python
class PackageSample:
	pass
```

Now the package and module can be imported: 

```python
from packages_sample.PackageSample import PackageSample

#
# ...
#
```

>Important: the \_\_init\_\_.py can be an empty file.