# Markup Extensions

From [Markup Extensions for XAML Overview](https://docs.microsoft.com/en-us/dotnet/framework/xaml-services/markup-extensions-for-xaml-overview)
> Markup extensions are a XAML technique for obtaining a value that is neither a primitive nor a specific XAML type. 
> For attribute usage, markup extensions use the known character sequence of an opening curly brace **{** to enter 
> the markup extension scope, and a closing curly brace **}** to exit. 
>
> When using .NET Framework XAML Services, you can use some of the predefined XAML language markup extensions from the System.Xaml assembly. You can also subclass from the [MarkupExtension](https://docs.microsoft.com/en-us/dotnet/api/system.windows.markup.markupextension?view=netframework-4.7.1) class, defined in System.Xaml, and define your own markup extensions. Or you can use markup extensions defined by a particular framework if you are already referencing that framework .


Our Markup Extensions:
- [Icon](icon.md)
- [Localization](localization.md)