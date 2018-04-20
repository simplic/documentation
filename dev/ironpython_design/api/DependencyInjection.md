DependencyInjection
===

Dependency injection module for python


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.DependencyInjection.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import DependencyInjection

# usage
DependencyInjection.METHOD(...)
```


## Properties

## Methods

### resolve
Get instance of a unity service

| Name | Summary |    |
| --- | --- | ---- |
 | type | Interface type | |

__Returns:__
Instance of an unity service

### resolve_with_key
Get instance of a unity service

| Name | Summary |    |
| --- | --- | ---- |
 | type | Interface type | |
 | key | Optional key | |

__Returns:__
Instance of an unity service
