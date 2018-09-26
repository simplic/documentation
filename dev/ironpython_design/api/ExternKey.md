ExternKey
===

Represents an external key


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.ExternKey.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import ExternKey

# usage
ExternKey.METHOD(...)
```


## Properties

### extern_identity_str

Gets or sets the extern identity as string

### extern_identity_int

Gets or sets the extern identity as long

### extern_identity_guid

Gets or sets the extern identity as guid

### ExternIdentityStr

Gets or sets the extern identity as string

### ExternIdentityInt

Gets or sets the extern identity as long

### ExternIdentityGuid

Gets or sets the extern identity as guid

### Context

Gets or sets the key context

### context

Gets or sets the key context

### TenantId

Gets or sets the tenant id

### tenant_id

Gets or sets the tenant id

## Methods

### #ctor
Initialize new extern key

| Name | Summary |    |
| --- | --- | ---- |

### #ctor
Create extern key

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | externStr | External identity value | |
 | context | Optional data context | |

### #ctor
Create extern key

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | externInt | External identity value | |
 | context | Optional data context | |

### #ctor
Create extern key

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | externGuid | External identity value | |
 | context | Optional data context | |
