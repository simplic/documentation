# MessageBox

The `LocalizedMessageBox` control is the default control for a pop-up window
It supports only one format, which we use for simplic as default. NuGet Package `Simplic.Studio.UI` required for use.

```C#
public static MessageBoxResult Show(string localizationKeyForMessageBoxText, string localizarionKeyForCaption, MessageBoxButton button, MessageBoxImage icon)
```

Important: No localizationService needed

## Example

```C#
LocalizedMessageBox.Show("box_text_key", "caption_text_key", MessageBoxButton.OK, MessageBoxImage.Information);
```
