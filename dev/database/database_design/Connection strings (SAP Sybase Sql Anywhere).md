# Connection strings (SAP Sybase Sql Anywhere)

Simplic connection strings for SAP Sybase Sql Anywhere databases requires the following properties:

`SERVER=<server>;DBN=<database>;UID=<user id>;PWD=<password>;CHARSET=UTF8;LINKS=TCPIP`

The charset is required to support german umlauts.

If a specific host is required, it must be placed after the `TCPIP` value:

`SERVER=<server>;DBN=<database>;UID=<user id>;PWD=<password>;CHARSET=UTF8;LINKS=TCPIP(host=<host address>)`

__ Hint: The `UserConnectionString` in `Studio.ini` doesn't need a `UID` and `PWD` __

For more information take a look at [SAP Sybase documentation](http://dcx.sybase.com/1201/en/dbadmin/connect-connection-string.html)