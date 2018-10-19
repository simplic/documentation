# Contextless reports

Contextless reports can be printed using the simplic print itembox from the start menu:

![~/images/epl-contextless.png](~/images/epl-contextless.png)

The number of the given sequence in the contextless report will be passed as `value`-parameter. The amount of copies are available in the `amount`-parameter.
A report design could look like this:

```
; Design

N
Q152,24
q418
;R130,10

B15,25,0,1,2,2,70,B,"{value}"

P{amount}
```

This design will print a simple barcode in the following format:

![~/images/barcode-result.png](~/images/barcode-result.png)

