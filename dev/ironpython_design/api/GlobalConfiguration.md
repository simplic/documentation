GlobalConfiguration
===

Module for working with sequences, e.g. generate new sequence numbers.


## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic.GlobalConfiguration.METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import GlobalConfiguration

# usage
GlobalConfiguration.METHOD(...)
```


## Properties

## Methods

### get_section
Get current section with which the studio was initialized

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Section as string, default is default

### get_str
Get global configuration value as string. All values are retrieved by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | use_cache | If set to true (default) the value will be cached after first retrieving | |

__Returns:__
Configuration value

### set_str
Set global configuration value (string-value). All values are stored by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | value | Value which will be stored as configuration | |

### get_int
Get global configuration value as integer. All values are retrieved by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | use_cache | If set to true (default) the value will be cached after first retrieving | |

__Returns:__
Configuration value

### set_int
Set global configuration value (int-value). All values are stored by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | value | Value which will be stored as configuration | |

### get_bool
Get global configuration value as boolean. All values are retrieved by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | use_cache | If set to true (default) the value will be cached after first retrieving | |

__Returns:__
Configuration value

### set_bool
Set global configuration value (boolean-value). All values are stored by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | value | Value which will be stored as configuration | |

### get_double
Get global configuration value as double. All values are retrieved by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | use_cache | If set to true (default) the value will be cached after first retrieving | |

__Returns:__
Configuration value

### set_double
Set global configuration value (double-value). All values are stored by the following key:
            config_name. plugin, username

| Name | Summary |    |
| --- | --- | ---- |
 | config_name | Name of the configuration | |
 | plugin | The plugin / part to which the configuration belongs | |
 | username | Username, is needed if user-specific values should be retrieved, else empty string | |
 | value | Value which will be stored as configuration | |
