# Working with Barcode Validation

In this code sample we will show how to validate a barcode with Python and Sql.

## Samples


# Python

```python
class BarcodeValidationSample: 

    def validate(self, barcode): 

        if '12345' in barcode: 
            return True 

        return False  
```

# SQL-Statement
```sql
Select 1 from dummy where ? like '12345%' 
```
***
