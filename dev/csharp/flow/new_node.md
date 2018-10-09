# Adding new Nodes

A flow system without nodes is basically useless. In order for it to work a flow system needs nodes. Luckily defining nodes is a piece of cake.

First create a class project and install `Simplic.Flow` via nuget. Then decide if the node supposed to be an `ActionNode` or an `EventNode`.

You need to decorate the class with `ActionNodeDefinition` or `EventNodeDefinition`. 

Sample Action Node:

```csharp
[ActionNodeDefinition(DisplayName = "Text displayed on the Editor", Name = "NameoftheNode", Category = "This will be used to show this node under the right list on the Editor")]
public class SampleNode : ActionNode
{
    ....
}
```

Sample Event Node:
```csharp
[EventNodeDefinition(DisplayName = "On Something Happened", Name = "OnSomethingHappenedNode", EventName = "OnSomethingHappened", Category = "IO")]
public class OnSomethingHappenedNode : EventNode
{
    ... 
}
```

After this definition, you need to define the pins. The pins are used to connect nodes. 

## Putting it all together

Here is a full action node definition:

```csharp
[ActionNodeDefinition(DisplayName = "Console out", Name = "ConsoleWriteLineNode", Category = "Common")]
public class ConsoleWriteLineNode : ActionNode
{
    public override bool Execute(IFlowRuntimeService runtime, DataPinScope scope)
    {
        var value = scope.GetValue<object>(InPinToPrint);
        System.Console.WriteLine(value);
            
        if (OutNode != null)
            runtime.EnqueueNode(OutNode, scope);

        return true;
    }

    [FlowPinDefinition(DisplayName = "Out", Name = "OutNode", PinDirection = PinDirection.Out)]
    public ActionNode OutNode { get; set; }

    [DataPinDefinition(
        Id = "b6ffc7b8-8f06-409c-8d27-7757518c2ab6", 
        ContainerType = DataPinContainerType.Single, 
        DataType = typeof(object), 
        Direction = PinDirection.In, 
        Name = "InPinToPrint",
        DisplayName = "To Print")]
    public DataPin InPinToPrint { get; set; }

    public override string FriendlyName { get { return nameof(ConsoleWriteLineNode); } }
    public override string Name { get { return nameof(ConsoleWriteLineNode); } }        
}
```

and a full event node:
 
```csharp
[EventNodeDefinition(DisplayName = "On Check Directory Content", Name = "OnCheckDirectoryContentNode", EventName = "OnCheckDirectoryContent", Category = "IO")]
public class OnCheckDirectoryContentNode : EventNode
{
    public override bool Execute(IFlowRuntimeService runtime, DataPinScope scope)
    {
        var args = runtime.FlowEventArgs as OnCheckDirectoryContentEventArgs;

        if (args == null)
        {
            Console.WriteLine($"Arguments not found in {nameof(OnCheckDirectoryContentNode)}");
            return false;
        }
        if (string.IsNullOrWhiteSpace(args.DirectoryPath))
        {
            Console.WriteLine($"Path null or mpety in {nameof(OnCheckDirectoryContentNode)}");
            return false;
        }

        scope.SetValue(OutPinDirectoryPath, args.DirectoryPath);

        if (!Directory.Exists(args.DirectoryPath))
        {
            Console.WriteLine($"Directory not found `{args.DirectoryPath}` {nameof(OnCheckDirectoryContentNode)}");
            return false;
        }

        if (OutPinDirectoryPath != null && Directory.GetFiles(args.DirectoryPath).Any())
        {
            runtime.EnqueueNode(OutNode, scope);
        }

        return true;
    }

    [FlowPinDefinition(DisplayName = "Out", Name = "OutNode", PinDirection = PinDirection.Out)]
    public ActionNode OutNode { get; set; }

    [DataPinDefinition(
        Id = "f980c0e6-5dc3-4064-8db7-c95b08d90664",
        ContainerType = DataPinContainerType.Single,
        DataType = typeof(string),
        Direction = PinDirection.Out,
        Name = "OutPinDirectoryPath",
        DisplayName = "Pin Directory Path")]
    public DataPin OutPinDirectoryPath { get; set; }

    public override string EventName
    {
        get
        {
            return "OnCheckDirectoryContent";
        }
    }

    public override string FriendlyName
    {
        get
        {
            return nameof(OnCheckDirectoryContentNode);
        }
    }

    public override string Name
    {
        get
        {
            return nameof(OnCheckDirectoryContentNode);
        }
    }
}
```

## Registering the node
In order to be able to use the node we just created, we need to register this node to the IoC (Unity in our case). 

You need to register your node with a node resolver, as all the nodes could behave differently but need to inherit a base node. Luckily we have a `GenericNodeResolver` to use for basic nodes.

Registering a node:

```csharp
container.RegisterType<INodeResolver, GenericNodeResolver<OnCheckDirectoryContentNode>>("OnCheckDirectoryContentNode");
```