# FleetBoard Python Script

A python script will be processed when executing fleetboard function resolver. 

This FleetBoard Python Script should reside under `repository\private\Telematic\Fleetboard\`

## Example:
Example python script file `TextMessage.py` for sending a text message to a vehicle:
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

## Parameters:
**telematic_configuration:**
This parameter is of type `FleetboardRequestConfiguration`. It contains the following properties:
```csharp
long StructureId
long ObjectTypeId
string VehicleIdentifier
Dictionary<long, string> Fields
```

Fields can be used to send parameters to the system.

**data:**

This parameter is of type `ITelematicContext` and has following property:
```csharp
string Name
```

and the following method:
```csharp
object GetData(Guid id)
```

For example context data for `ShipmentContextResolver` returns a `Shipment` object.

**pay_load:**

This parameter carries a value that can be obtained from the user. This could be of any type. It depends on the function resolver.