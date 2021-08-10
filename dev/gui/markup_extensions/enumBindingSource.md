# Enum Binding Source MarkupExtension

## Usage EnumBindingSource

To use the EnumBindingSource simply reference the Simplic.Studio package and add a reference to the xaml.
In this example it's named 'studio'. 
To specify the enum use x:Type as show in this example. Here it is the 'FieldDataType' in our 'local' namespace.

\<ComboBox ItemsSource="{Binding Source={studio:EnumBindingSource {x:Type local:FieldDataType}}}"/>

For a simple binding without alias/user-friendly text this is all you need to do to get your enum as a itemsource.


## Usage EnumDescriptionTypeConverter

If you need to give your enums an alias for example to display a german translation you can use the EnumDescriptionTypeConverter.
To use it you need to define the 'Description' attribute above your enum values (see code snippet below).
Aswell as doing that you also need to define the typeconverter for your enum with the attribute of the same name.
In addion to that you need to give the attribute the type of converter you want to use, which is the 'EnumDescriptionTypeConverter'.
After you have set both of this you should see your description text displayed in the combobox

    [TypeConverter(typeof(EnumDescriptionTypeConverter))]
    public enum FieldDataType
    {
        [Description("Text")]
        String = 0,
        [Description("Zahl")]
        Int = 1,
        [Description("Dezimalzahl")]
        Double = 2,
        [Description("Datum")]
        DateTime = 3
    }


Source: https://brianlagunas.com/a-better-way-to-data-bind-enums-in-wpf/
