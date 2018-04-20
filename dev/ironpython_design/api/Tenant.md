Tenant
===

API tenant


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.Tenant.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import Tenant

# usage
Tenant.METHOD(...)
```


## Properties

### name

Name for usage

### id

Unique id

### connection_id

The tenant's connection string

### extern_name

Name of the tenant in the external system

### extern_id

ID of the tenant in the external system

## Methods

### #ctor
Create new tenant instance

| Name | Summary |    |
| --- | --- | ---- |
 | _tenant | Internal tenant instance | |

### #ctor
Initialize new tenant

| Name | Summary |    |
| --- | --- | ---- |
