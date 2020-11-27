Sql-Log
===

To log all SQL statements executed by Simplic Studio / Application Server,
the corresponding application must be started with the argument `--debug-area sql`. Afterwards it will create a log file under: `%localappdata%\\Simplic Studio\\<<Section>>\\Log\\sql.Simplic.log`.
This file contains the executed statements.

**Note**

Importer scripts are currently not included.