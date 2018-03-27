# Localization Markup Extension
**Requires:** `Simplic.Localization.UI` from NuGet.

## Usage
Add simplic xmlns to the top of the page:
```xml
xmlns:simplic="http://schemas.simplic-systems.com/2016/xaml/presentation"
```

Make sure you define a translation key in the translation file in the repository under:
`{repo}/Localization/file.{language}.json` 
where **repo** could be private or public, and **language**: de-DE or en-US

Example **language.en-US.json**
```json
{
    "langHello": "Hello",
    "langWorld": "world"
}
```

Example **language.de-DE.json**
```json
{
    "langHello": "Hallo",
    "langWorld": "welt"
}
```

Then use it like any other markup extension:
```xml
<Label Content="{simplic:Localization Key=langHello}" />
<Label Content="{simplic:Localization Key=langWorld}" />
```
