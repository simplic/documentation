> Please note that this a WIP document. Any feedback is welcome.
> Contact me at [yavuz.guenay@simplic.biz](mailto:yavuz.guenay@simplic.biz)
# Dependency Injection
## What is dependency injection ?
Dependency injection is a very simple concept.

Stack overflow user [wds](https://stackoverflow.com/users/10098/wds) in [this](https://stackoverflow.com/a/130862/2047029) thread explains it perfectly:
>Basically, instead of having your objects creating a dependency or asking a 
>factory object to make one for them, you pass the needed dependencies in to the object externally, 
>and you make it somebody else's problem. This "someone" is either an object 
>further up the dependency graph, or a dependency injector (framework) that 
>builds the dependency graph. 
>
>A dependency as I'm using it here is any other object the current object 
>needs to hold a reference to.
>
>One of the major advantages of dependency injection is that it can make 
>testing lots easier. 

A detailed information can be found 
[here](https://msdn.microsoft.com/en-us/library/dn178470(v=pandp.30).aspx).

Basically it makes our projects more maintainable, loosely coupled but most 
importantly it makes our code testable.

## How to use ?
We use the [Unity Container](https://msdn.microsoft.com/en-us/library/ff647202.aspx) as our dependency injection framework.

Usually there will be one container in the application lifetime created in startup.
 We register types (or instances) into the container and somewhere else when we 
need these types, we simply put the interfaces of these type in our constructor. There are
instances where we cant register types to our container so we use [ServiceLocator](https://msdn.microsoft.com/en-us/library/ff648968.aspx) 
to resolve the types at run time.

You can install [Unity](https://www.nuget.org/packages/Unity/) via NuGet. 

**Registering and Resolving Types :**

Using dependency injection requires a little bit of mindset changing. 
Traditionally we would create classes and create new instances of our 
dependencies. In order to remain loosely coupled and 
testable, we now let the container resolve the dependencies for us. 
For that, types must be registered in the container using an interface. 
We will use these interfaces later on to get the actual implementations 
registered in the container.

Here is an example of who we do it traditionally:
```csharp
public class ClientManager : IClientManager
{
    private readonly DataAccess;
    private readonly Emailer;
    private readonly Logger;

    public ClientManager()
    {
        DataAccess = new DataAccess();
        Emailer = new Emailer();
        Logger = new Logger();
    }

    ...
}
```

As you can see we create instances of our dependencies in the constructor. This
approach kills the possibility of unit testing. 

**Doing it right:**

```csharp
public interface IDataAccess { ... }
public class DataAccess : IDataAccess { .. }

public interface IEmailer { .. }
public class Emailer : IEmailer { .. }

public interface ILogger { .. }
public class Logger : ILogger { .. }

// in Program.cs 
var container = new UnityContainer();

// ContainerControlledLifetimeManager means "Register a singleton type"
// custom life time managers are possible
container.RegisterType<ILogger, Logger>(new ContainerControlledLifetimeManager());

// you can also register same types with different names
container.RegisterType<IDataAccess, DataAccess>("Unique Name 1");
container.RegisterType<IDataAccess, DataAccess>("Unique Name 2");

container.RegisterType<IEmailer, Emailer>();

// at this point unity would resolve all the types (interfaces) 
// that are in the constructor 
// Carefull, the types that are needed must be registered before this line
container.RegisterType<IClientManager, ClientManager>();


// somewhere in your project
public class ClientManager : IClientManager
{
    ...

    public ClientManager(IDataAccess dataAccess, IEmailer emailer, ILogger logger)
    {
        // do something with your dependencies
    }
}
```

## Using ServiceLocator

In cases where you dont have access to the container you can use a 
Service Locator. You can find detailed information on ServiceLocators
[here](https://msdn.microsoft.com/en-us/library/ff648968.aspx).

First you need to install [CommonServiceLocator](https://www.nuget.org/packages/CommonServiceLocator/) from NuGet. 
Then in your constructor call ServiceLocator to get an instance of a type you need as 
follows:

```csharp

// somewhere in your project
public class ClientManager : IClientManager
{
    ...

    public ClientManager()
    {
        dataAccess = ServiceLocator.Current.GetInstance<IDataAccess>();
        emailer = ServiceLocator.Current.GetInstance<IEmailer>();
        logger = ServiceLocator.Current.GetInstance<ILogger>();

        // do something with your dependencies
    }
}
```
