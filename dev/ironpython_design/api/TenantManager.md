TenantManager
===

Tenant public API


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.TenantManager.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import TenantManager

# usage
TenantManager.METHOD(...)
```


## Properties

## Methods

### get_by_id
Get a tenant by its unique id

| Name | Summary |    |
| --- | --- | ---- |
 | id | Unique tenant id | |

__Returns:__
Tenant instance if found, else None

### get_by_name
Get a tenant by its unique name

| Name | Summary |    |
| --- | --- | ---- |
 | name | Unique tenant name | |

__Returns:__
Tenant instance if found, else None

### get_connection_name
Get a connection string name by a tenant instance

| Name | Summary |    |
| --- | --- | ---- |
 | tenant | Tenant instance which is connected with a connection string | |

__Returns:__
Connection string name

### get_connection_name
Get a connection string name which belongs to an extern key

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key instance | |

__Returns:__
Connection string name

### get_connection_string
Get a connection string if set by a tenant instance

| Name | Summary |    |
| --- | --- | ---- |
 | tenant | Tenant instance which is connected with a connection string | |

__Returns:__
Connection string information

### get_connection_string
Get a connection string which belongs to an extern key

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key instance | |

__Returns:__
Connection string information

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_guid | Internal identity | |

__Returns:__
None

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_int | Internal identity | |

__Returns:__
None

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_str | Internal identity | |

__Returns:__
None

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_guid | Internal identity | |
 | context | Data context | |

__Returns:__
None

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_int | Internal identity | |
 | context | Data context | |

__Returns:__
None

### get_extern_identity
Get an extern key by passing the primary key (unique tenant, internal identity)

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant guid | |
 | intern_identity_str | Internal identity | |
 | context | Data context | |

__Returns:__
None

### set_extern_identity
Save an external identity

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key instance | |
 | internIdentityGuid | Identity value | |

### set_extern_identity
Save an external identity

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key instance | |
 | internIdentityInt | Identity value | |

### set_extern_identity
Save an external identity

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key instance | |
 | internIdentityStr | Identity value | |

### remove_by_identity_str
Remove by tenant and intern identity tuple

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | intern_str | Intern identity | |

### remove_by_identity_int
Remove by tenant and intern identity tuple

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | intern_int | Intern identity | |

### remove_by_identity_guid
Remove by tenant and intern identity tuple

| Name | Summary |    |
| --- | --- | ---- |
 | tenant_id | Unique tenant id | |
 | intern_guid | Intern identity | |

### remove_by_extern_key
Remove all key by it's extern-key

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key which contains the extern id information | |

### remove_by_extern_key_ignore_tenant
Remove all keys by an extern key and ignore the given tenant. So data will be removed for ALL tenants.

| Name | Summary |    |
| --- | --- | ---- |
 | key | Key which contains the extern id information | |
