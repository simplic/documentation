# Working with the Printermanager to get the printer name. 

In this code sample we will show how to use the PrinterManager in the Simplic Framework to get the printer name for the current user. The following script returns the printer name including redirections.

## Required Modules

- [Simplic.Printing](xref:Simplic.Printing)
  - [PrinterManager](xref:Simplic.Printing.PrinterManager)

## Samples


# Python

```python
from Simplic.Printing import PrinterManager

configuration = PrinterManager.Singleton.GetConfiguration("BarcodepPinter")
redirected_queue_name = configuration.Device.QueueName
```
***

## Expected Output
```
E.g. the user has redirected Barcodeprinter to TPL2048, TPL2048 will be returned. If no redirection is set, Barcodeprinter will be returned.
```
