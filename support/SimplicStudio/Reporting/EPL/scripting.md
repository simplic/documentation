# EPL script integration

EPL reports can be printed using the simplic python api:

```py
from simplic import EPLReportManager

EPLReportManager.print_report("<report-name>", "<optional-printer-name>", "<optional-parameter-dictionary>")
```

If a printer is passed to the method, it will be used for printing the report. The name must be a simplic printer name.
If the report design requires parameter, it can be passed as python dictionary:

```py
from simplic import EPLReportManager

parameter =	{
  "barcode": "BC1234567890",
  "copies": "20"
}

# 21 copies with the barcode BC1234567890 will be printed
# 20 + 1 in the report design
EPLReportManager.print_report("SampleReport", None, parameter)
```

Design:

```
; Design

@{
	amount = copies + 1
}@

N
Q152,24
q418
;R130,10

B15,25,0,1,2,2,70,B,"{barcode}"

P{amount}

```

The parameters passed to the method are available in the report.
