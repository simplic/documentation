# Sql Service

We are using a service approach to make database requests. 

The following code shows an example:
```csharp
// get a reference to the sql service
private readonly ISqlService sqlService;


// then somewhere in a method

public string GetString(Guid id)
{
    return sqlService.OpenConnection( (connection) =>
    {
        return connection.Query<string>("SELECT TableName 
            FROM {TableName} WHERE Guid = :Guid", new { Guid = id })
            .FirstOrDefault();
    });    
}
```