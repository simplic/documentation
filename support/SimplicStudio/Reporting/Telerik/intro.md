# Telerik reporting

Simplic has an integration for telerik reporting. The integration allows you to create, edit and print reports. Reports can be printed using a simplic printer or to pdf. The simplic printer system will redirect the print job to a windows printer queue.

## Report store

Reports are stored in the simplic Repository under `/built-in/Reports/`. There is no need to deploy reports to any machine. Privatized reports starts with `private.`.
Currently the Telerik `.trdx` file extension is used.

## Creating new report

New reports must be created using the report management under the `Configuration/Reporting/Telerik-Reports` section. Before a new report is created, you must decide between three times of reports: 

1. [Sql report](sql-report.md) 
2. [Key-Value report](key-value-report.md) 
3. [Parameter report](parameter-report.md)

## Connection string and provider

Within the simplic report configurator a connection string name and provider is selectable. This settings will override all **sql data source settings** within the report. The connection string setting requries a simplic connection string name or a full qualified connection string. A connection string name is suggested. Simplic currently supports two provider:

1. SAP Sql Anywhere 16 (`iAnywhere.Data.SqlAnywhere.EF6`)
2. ODBC (`System.Data.Odbc`)

If the odbc provider is selected, the required odbc driver must be installed on any machine for printing the report.

![~/images/report-connection.png](~/images/report-connection.png)

> Simplic connection strings are located under the administration section.

## Check-in and check-out

Since reports are not stored in the windows file system rather than the simplic repository, they needs to be checked-out for editing. A report can only be checked-out by one user at a time to prevent conflicts. After editing a report, it must be checked-in to publish all changes. The checkout state can be undon, if the changes should be discard.

## Privatize an existing report

A privatized report will not be updated using a simplic setup. To privatize a report just check the given checkbox in the report configuration editor:

![~/images/privatize-report.png](~/images/privatize-report.png)