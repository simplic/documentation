# Printer scripting integration

Reports can be printed using the simplic printer system. Telerik reports and epl reports can be printed directly using the python api for EPL- and Telerik-Reports.


## Print IPrintable

To print an object that inherits from `IPrintable` the `PrintManager` can be used:

```py
from Simplic.Printing import PrinterManager

printer = PrinterManager.Singleton.GetConfiguration("<printer-name>")
printer.Print(<printable-object>)
```

A sample implementation is the `PrintablePdf`-object in the simplic framework.