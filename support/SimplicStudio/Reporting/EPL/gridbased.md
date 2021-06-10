# EPL grid integration

EPL reports can be printed directly from a simplic grid view. To print an epl report from a context menu, the following configuration is required:

![~/images/grid-epl.png](~/images/grid-epl.png)

The `Quickreport`-name must be the same as the report configuration name. The type of the report must be *grid based*. All selected columns are available as parameter in the report design:

If the grid statement looks like this:

```sql
SELECT
  Id
, Barcode
, Name
FROM Sample
```

The parameter can be used like that:

```
; Design

N
Q152,24
q418
;R130,10

B15,25,0,1,2,2,70,B,"{barcode}"

P{amount}
```

Important: All column-names in the Report-Design must be written in lower-case.

The `amount`-parameter is reserved for the amount of copies from the default dialog.
