# EPL report configuration

The epl report configurator is located under `Configuration/Reporting/EPL-Reports`. The main options in the configuration secion are:

* Intern name - A unique intern name of the report. This is important for grid based and api based printing
* Display name - Dispaly name / driendly name
* Design - The report design that determines the layout and available parameter of the report
* Printer - Default printer. The printer must be of type `Label`-printer
* Data source - The data source decides where the data came from
 * None - No data source. The data must be passed manually
 * Sequence - The data are generated using a sequence number
 * Grid - The data will be passed by a grid
 * Sql - The data will be passed from the sql statement in the report configurator (Columns are available as parameter)
* Number sequence - Sequencen number as data source. The values will be passed in the `value`-parameter
* Sql - Sql as data source
* Contextless - If this option is set, the report is contextless printable

![~/images/epl-report-configuration.png](~/images/epl-report-configuration.png)

