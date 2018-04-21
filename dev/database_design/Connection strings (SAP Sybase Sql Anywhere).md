# Connection strings (SAP Sybase Sql Anywhere)

Simplic connection strings for SAP Sybase Sql Anywhere database requires the following properties:

`SERVER=<server>;DBN=<database>;UID=<user id>;PWD=<password>;CHARSET=UTF8;LINKS=TCPIP`

The charset is required to support german umlauts.

If a specific host is required, it must be placed after the `TCPIP` value:

`SERVER=<server>;DBN=<database>;UID=<user id>;PWD=<password>;CHARSET=UTF8;LINKS=TCPIP(host=<host address>)`

> Hint: The `UserConnectionString` in `Studio.ini` doesn't need a `UID` and `PWD`