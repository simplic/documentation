## DB

A single CosmosDB database is used as a data storage for all microservices. Some points to mention:
- All interaction with DB is done via IRepository. An exception is User collection - it's managed via ASP.NET Core Identity tools (UserStore, UserManager)
- Every document is derived from BaseDocument and therefore has Id of type GUID, OrganizationId of type GUID and IsDeleted flag
- all deletes are soft (i.e. nothing is removed from DB, instead IsDeleted field is set to `true`)
- almost all collections are sharded by OrganizationId
