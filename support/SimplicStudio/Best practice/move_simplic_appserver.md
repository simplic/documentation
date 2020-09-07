# Move simplic app-server and database to a new windows server

The following steps have to be considered when copying or migrating a Simplic Studio installation to a new Windows server.

1. Install SAP Sybase SQL-Anywhere components
2. Install Simplic Studio Setup in the correct version
3. Copy database to the new server
4. Set up database service and adapt Studio.ini
5. Start Simplic Studio and update all licenses under Administration
6. Start application server and assign modules. After module assignment, the application servers must be restarted
7. The server name must be adjusted in the flow and schedule configuration
8. File paths used in flows must be adjusted