> Please note that this a WIP document. Any feedback is welcome.

# Repository Pattern
We use repository pattern to abstract data persistence logic in simplic. 
We dont use unit of work pattern, instead we have services.

**Note:** we use [Dapper](https://github.com/StackExchange/Dapper) as our [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping).

## What is it ?

Check **[this](https://stackoverflow.com/a/11985962/2047029)** stack overflow answer for a short explanation.

## How to use it ?

First define an interface:
```csharp
public interface IUserRepository
{
    /// Dont forget to add summary
    IEnumerable<User> GetAll();
    User GetById(Guid id);
    ..
}
```

then implement the interface:
```csharp
public class UserRepository : IUserRepository
{
    public IEnumerable<User> GetAll()
    {   
        using (var connection = ConnectionManager.GetOpenPoolConnection<SAConnection>())
        {
            return connection.Query<User>($"SELECT * FROM {TableName}");
        }
    }

    public User GetById(Guid id)
    {   
        using (var connection = ConnectionManager.GetOpenPoolConnection<SAConnection>())
        {
            return connection.Query<User>($"SELECT * FROM {TableName} WHERE Id = :id", new { id })
                .FirstOrDefault();
        }
    }
}
```