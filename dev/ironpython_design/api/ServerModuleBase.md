
===




## Import and usage of the module
### Calling any static methods
Using simple `import simplic` statement
```
import simplic

# usage
simplic..METHOD(...)
```
Using simple `from simplic import ...` statement
```
from simplic import 

# usage
.METHOD(...)
```


## Properties

### min_sleep_time

Minimal thread sleep time

### execute_at

Time where the execute would be started every day

## Methods

### #ctor
Create service module, will be called internal

| Name | Summary |    |
| --- | --- | ---- |
 | module_guid | Unique guid of the module | |

### LoadModule
Only for internal use, returns load_module

| Name | Summary |    |
| --- | --- | ---- |
 | serviceName | service name | |
 | maschineName | Maschine name | |

__Returns:__
return load_module

### load_module
Will be executed when loading the module and desides, whether it will be available on the specific machine/service. Should return true if it will be available.

| Name | Summary |    |
| --- | --- | ---- |
 | service_name | Name of the starting service | |
 | machine_name | Name of the starting machine | |

__Returns:__
None

### Start
Only for internal use

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Return start() return value

### start
Start the module and created the main thread and register it

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Must return true, if the module should be used

### __do__
Will started in a nother thread and executes by default the main loop of the module.

| Name | Summary |    |
| --- | --- | ---- |

### execute
Will be executed for executing scripting tasks. Will be executed by default every 100ms, can be changed using self.min_sleep_time = ....

| Name | Summary |    |
| --- | --- | ---- |

__Returns:__
Should return true, until the module has to be quit

### set_execute_at
Sets the execute_at property

| Name | Summary |    |
| --- | --- | ---- |
 | hours | None | |
 | minutes | None | |

### SyncUpdate
Sync update, will not be published

| Name | Summary |    |
| --- | --- | ---- |
 | delta | Time since last frame | |
