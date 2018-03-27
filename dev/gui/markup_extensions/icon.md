# Icon Markup Extension
**Requires:** `Simplic.Icon.UI` from NuGet.

## Usage
Add simplic xmlns to the top of the page:
```xml
xmlns:simplic="http://schemas.simplic-systems.com/2016/xaml/presentation"
```

Then use it like any other markup extension:
```xml
<Image Source="{simplic:Icon Name=delete_16x}" />
```

You can either use **Name** or **Id** parameter to show an Icon.