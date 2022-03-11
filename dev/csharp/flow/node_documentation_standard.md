# Flow Node Documentation Standard

## Basics:
The flow node documentation works in the same way as the standard API documentation for classes, methods and properties by using XAML tags in front of classes that constitute nodes and properties that constitute pins.

In some cases the documentation_config.json file in the root directory of a repository containing flow nodes must be modified so that projects containing the nodes aren't excluded from the documentation.

## Node:
The class of each node is preceded by an XAML summary containing at least a short description of the node's function in one or at maximum two sentences.

This description can be further extended by the use of an XAML paragraph containing a more detailed description and additional functionality the node provides.

### Example:
```csharp
    /// <summary>
    /// Extracts a barcode from a .tif or .pdf file.
    /// <para>Provides additional functionality to convert the input file to black-and-white.</para>
    /// </summary>
    [ActionNodeDefinition(DisplayName = "Read Barcode", Name = nameof(ReadBarcodeNode), Category = "Barcode", Tooltip = "Reads barcode from image (tif) or pdf")]
    public class ReadBarcodeNode : ActionNode
    {
        ...
```

## Flow pins:
Each outgoing flow pin property is preceded by an XAML summary describing what triggers it.

An additional more abstract/contextual description further explaining the pin's purpose can be provided in an added XAML paragraph.

### Example 1:
```csharp
        /// <summary>
        /// Triggers for each extracted barcode.
        /// </summary>
        [FlowPinDefinition(DisplayName = "Each barcode", Name = nameof(OutNodeEachBarcode), PinDirection = PinDirection.Out)]
        public ActionNode OutNodeEachBarcode { get; set; }
```

### Example 2:
```csharp
        /// <summary>
        /// Triggers when the barcode extraction was successful.
        /// </summary>
        [FlowPinDefinition(DisplayName = "Success", Name = "OutNodeSuccess", PinDirection = PinDirection.Out)]
        public ActionNode OutNodeSuccess { get; set; }
```

## Data pins:
Each data pin property is preceded by an XAML summary containing what kind of data the pin accepts or provides and the data type.

An additional more abstract/contextual description further explaining the pin's purpose can be provided in an added XAML paragraph.

### Example 1 InPin:
```csharp
        /// <summary>
        /// Accepts the formats of the barcodes to be extracted as a list of string.
        /// </summary>
        [DataPinDefinition(
            Id = "eeb5ae9a-f91f-4a74-accf-a92b235c1d17",
            ContainerType = DataPinContainerType.Single,
            DataType = typeof(string),
            Direction = PinDirection.In,
            Name = "InPinBarcodeFormats",
            DisplayName = "Barcode Formats")]
        public DataPin InPinBarcodeFormats { get; set; }
```

### Example 2 InPin:
```csharp
        /// <summary>
        /// Accepts the information whether to convert to black-and-white or not as a boolean.
        /// </summary>
        [DataPinDefinition(
            Id = "8ce72447-9680-4aa1-949d-e16a66626645",
            ContainerType = DataPinContainerType.Single,
            DataType = typeof(bool),
            Direction = PinDirection.In,
            Name = nameof(InPinConvertBlackAndWhite),
            DisplayName = "Convert black-and-white")]
        public DataPin InPinConvertBlackAndWhite { get; set; }
```

### Example 1 OutPin:
```csharp
        /// <summary>
        /// Provides the barcode recognition results as a list of BarcodeRecognitionResult.
        /// </summary>
        [DataPinDefinition(
            Id = "e9e0bd5d-46af-4f4c-9878-376e6ba53db6",
            ContainerType = DataPinContainerType.Single,
            DataType = typeof(IList<BarcodeRecognitionResult>),
            Direction = PinDirection.Out,
            Name = nameof(OutPinBarcodePages),
            DisplayName = "Barcode Pages")]
        public DataPin OutPinBarcodePages { get; set; }
```

### Example 2 OutPin:
```csharp
        /// <summary>
        /// Provides the containing page number for each barcode as a string.
        /// </summary>
        [DataPinDefinition(
            Id = "00b53f8d-167a-4de1-8ef3-af43e4602882",
            ContainerType = DataPinContainerType.Single,
            DataType = typeof(string),
            Direction = PinDirection.Out,
            Name = nameof(OutPinCurrentBarcode),
            DisplayName = "Current barcode")]
        public DataPin OutPinCurrentBarcode { get; set; }
```