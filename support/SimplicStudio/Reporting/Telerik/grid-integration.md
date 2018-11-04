# Grid integration

Sql and key-value reports are integratable with simplic grids. A report can be printed and shown by using the Quick-Report options in the menu settings.
The name of the report must be entered in the `Quickreport` field. If the option for printing the report directly is checked, the report will be printed on the default printer.
The default printer is option is located in the report [configuration](intro.md).

Furthermore there are two report viewer options. The first option is to open every report in a new window. The second option is to reuse an existing window:

![~/images/reporting-grid-options.png](~/images/reporting-grid-options.png)

## Using Sql report

If the target report is a sql report, the grid sql will be passed to the sql data source of the report.

## Using Key-Value report

If the target report is a key-value report, all columns will be passed as key-value list to the report. A parameter can be used by adding an `@` in front of the name.

If the sql statement in the grid looks like this:

```sql
SELECT
  Guid
, FirstName
FROM SampleColumn
```

The following parameter can be used in the telerik sql data source:

```sql
SELECT Column1, Column2 FROM Sample WHERE Gudi = @Guid
```
