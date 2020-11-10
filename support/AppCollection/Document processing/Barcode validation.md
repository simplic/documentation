# Barcode Validation WIP

## What is Barcode Validation? 
Barcode Validation filters out from all scanned barcodes the barcodes that are decisevely for the user. Under which conditions the barcodes are filtered, 
can be configured using the Configurator, Python scripts and Sql-Statements. 
The validation splits up all the Barcodes to have a document for each Barcode because it could happen that there's more than one barcode on a scanned page. 

## The configurator in Simplic

The configurator is the "filter" of the barcodes and can be configurated as you want.


To open the configurator you have to open Simplic and select the tab **Konfiguration** and then **Barcode-Validierung**.


If you want to create a new Barcode Validation Source you have to click on **Neue Quelle** and on the right side in Simplic is now a new Barcode Validation source to configure.

The default setting is a new source with SQL as type but you can decide between SQL and Python.


![~/images/barcode-validation-sql.png](~/images/barcode-validation-sql.png)

You can give the new source a name, a tenant/client and in this case (when SQL is selected) you can write the SQL-Statement in the textfield **SQL**
If you select Python it looks like this:

![~/images/barcode-validation-python.png](~/images/barcode-validation-python.png)

Here you have to enter the path of the python script and the name of the class.

## Configuration with Python

Writing a python script for the Barcode validation can be very simple. You need a class and you can use the method **validate** to validate a barcode.

### Python Script Sample

```py
class BarcodeValidationSample: 

    def validate(self, barcode): 

        if '12345' in barcode: 
            return True 

        return False  
```
If **12345** is in the barcode the script returns *true* if not *false*.