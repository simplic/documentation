# Get printer name including redirection

Using the `PrinterManager` in the Simplic Framework it is possible, to get the printer name for the current user. The following script returns the printer name including redirections:

```python
from Simplic.Printing import PrinterManager

configuration = PrinterManager.Singleton.GetConfiguration("BarcodepPinter")
redirected_queue_name = configuration.Device.QueueName
```

E.g. the user has redirected `Barcodeprinter` to `TPL2048`, `TPL2048` will be returned. If no redirection is set, `Baroceprinter` will be returned.
