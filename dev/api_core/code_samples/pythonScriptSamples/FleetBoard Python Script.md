# Working with 

In this code sample we will show to write a FleetBoard Python Script

## Required Modules

- [ITelematicContext](xref:Simplic.Telematic.Core.ITelematicContext)
- [FleetboardRequestConfiguration](xref:Simplic.Telematic.FleetBoard.FleetboardRequestConfiguration)

## Samples


# Python

```python
class FleetboardTextMessage:

    def fill(self, telematic_configuration, data, pay_load):
        telematic_configuration.StructureId = 1111111111
        telematic_configuration.ObjectTypeId = 2222222222
        telematic_configuration.VehicleId = 3333333333

        telematic_configuration.Fields.Add(1, "Test")
        telematic_configuration.Fields.Add(2, pay_load)

        return True
```
***

## Required  parameters and objects
```python
# Parameter of type FleetboardRequestConfiguration
# telematic_configuration: 
long StructureId
long ObjectTypeId
# Fields can be used to send parameters to the System  
string VehicleIdentifier
Dictionary<long, string> Fields

# Parameter of type ITelematicContext 
# data:
string Name
object GetData(Guid id)

#pay_load:
This parameter carries a value that can be obtained from the user. This could be of any type. It depends on the function resolver.

```