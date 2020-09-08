# MessageBox

The `MessageBox` control is the default control for a pop-up window
It supports multiple formats, but we only use the one below

```C#
public static MessageBoxResult Show(string messageBoxText, string caption, MessageBoxButton button, MessageBoxImage icon)
```

Important: Use the localizationService to translate the key

## Example

```C#
MessageBox.Show(localizationService.Translate("box_text_key"), localizationService.Translate("caption_text_key"), MessageBoxButton.OK, MessageBoxImage.Information);
```
