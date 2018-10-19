# Report design

Reports are designed in the epl printer language. The simplic integration enables a mixture of epl and python. Parameter that are passed to a report design are available as 
python parameter. More information about epl can be accessed [here](https://en.wikipedia.org/wiki/Eltron_Programming_Language). The editor is located under `Configuration/Reporting/EPL-Designs`. A report design requires an intern- and display-name:

![~/images/Report-Designer.png](~/images/Report-Designer.png)

Comments starts with `;`.

```
; Design

; Clear buffer / start new report
N

; Set label size
Q152,24

; Set label with
q418

; Set relative location of the following elements (e.g. barcode)
;R130,10

; Embed barcode label
B15,25,0,1,2,2,70,B,"{value}"

; Start printing, with "n" copies
P{amount}
```

Variables can be embedded into the string by enclosing them into braces: `{<parameter-name>}`. Parameter can be manipulated by embedding python scripts into a report design:

```
; Design
; Increase the amount by one
@{
	amount = amount + 1	
}@

; Clear buffer
N

; Set label size
Q152,24

; Set label with
q418

; Set relative location of the following elements (e.g. barcode)
;R130,10

; Embed barcode label
B15,25,0,1,2,2,70,B,"{value}"

; Start printing, with "n" copies
P{amount}
```
Scripts can be embedded by enclosing them into @-chars and braces:

```
@{
	# Script goes here
}@
```

Since the scripting language is python, the standard python syntax must be used.