# Simplic Flow System

Simplic Flow System is actually a work flow system. It allows us to automatize trivial tasks by designing them using the flow editor. As this is a technical documentation, we'll dive right into the details.

## How does it work ?
All flow configuration files ([sample configuration file](sample_configuration.md)) are loaded when the flow service starts. Flows start or pause by an event. Events trigger the flow service to either create new flow instances or continue processing them. When a flow instance is paused because of an event, the state is saved to be continued later on when that event occurs.

Every flow configuration consists of a bunch of nodes and connections between nodes' pins. 

There are two distinctive node types: **ActionNode** and **EventNode**.

### Action Node:
Action nodes have an abstract method called `public override bool Execute(IFlowRuntimeService runtime, DataPinScope scope)` 
which gets called whenever the node is to be processed.

### Event Node:
Event nodes also have an abstract method and an event name. Event name is important for the node to be triggered at the right event.


Every node has pins and pins have different types.

### Flow Pin:
Flow pins are used for execution flow. They are simple links between nodes. 

A flow pin has the following properties:

Property | Type |  Explanation
--- | --- | ---
`DisplayName` | `string` | Used to show a text in the node header
`Name` | `string` | Node's name.  
`Tooltip` | `string` | Tooltip to show on the editor
`PinDirection` | [PinDirection](pin_direction.md) | Pin direction decides the position (left, right) 
`AllowMultiple` | `bool` | You can connect to multiple flow pins if this is true, default is **false**.

A sample flow pin definition:
```csharp
[FlowPinDefinition(DisplayName = "Out", Name = "OutNode", PinDirection = PinDirection.Out, AllowMultiple = false)]
public ActionNode OutNode { get; set; }
```

### Data Pin:
Data pins are more complicated than flow pins, as they can have data type within them. 

A data pin has the following properties:

Property | Type |  Explanation
--- | --- | ---
`Id` | `string` | Unique Guid inside the node.
`DisplayName` | `string` | Used to show a text in the node header
`Name` | `string` | Node's name.  
`Tooltip` | `string` | Tooltip to show on the editor
`ContainerType` | [DataPinContainerType](data_pin_container_type.md) | Decides if the pin is a list or a single type
`DataType` | `Type` | Pin data type. Leave empty if `IsGeneric` is true.
`Direction` | [Direction](pin_direction.md) | Pin direction decides the position (left, right) 
`DefaultValue` | `object` | Default value of the pin, it is used if  no  pin is connected to this pin
`IsGeneric` | `bool` | Decides if the pin is a generic one. 
`AllowedTypes` | `string` | Used if `IsGeneric` is true. Types to be able to connect to this pin. Can be a list seperated by a comma. Should be in form of `Type.Name`.  e.g.: `Int16,UInt16,UInt32`

A sample data pin definition:

```csharp
[DataPinDefinition(
    Id = "b6ffc7b8-8f06-409c-8d27-7757518c2ab6", 
    DisplayName = "To Print"
    Name = "InPinToPrint",
    Tooltip = "To Print",
    ContainerType = DataPinContainerType.Single, 
    DataType = typeof(object),
    Direction = PinDirection.In, 
    DefaultValue = null,
    IsGeneric = false,
    AllowMultiple = false,
    )]
public DataPin InPinToPrint { get; set; }
```