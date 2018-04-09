> Please note that this a WIP document. Any feedback is welcome.

# Service Pattern (Microservices)

We use services to decouple business logic and repository. We like to keep our repositories as clean as possible.

# What is it ?
A quote from [Wikipedia](https://en.wikipedia.org/wiki/Microservices)
>Microservices is a software development technique—a variant of the service-oriented architecture (SOA) architectural style that structures an application as a collection of loosely coupled services. 
>In a microservices architecture, services are fine-grained and the protocols are lightweight. 
>The benefit of decomposing an application into different smaller services is that it improves 
>modularity and makes the application easier to understand, develop and test. 
>
>It also parallelizes development by enabling small autonomous teams to develop, 
>deploy and scale their respective services independently.
>It also allows the architecture of an individual service to emerge through continuous 
>refactoring. Microservices-based architectures enable continuous delivery and deployment.

# How to use it ?
First define the interface:

```csharp
public interface IUserService
{
    IEnumerable<User> GetAll();
    int CalculateUserAge(Guid id);    
    ..
}
```

**Note:** We derive our interface from repository so we dont have to repeat available methods in our service. It is perfectly fine to define same methods here as well but we like to keep things clean.

Then write the implementation of it:
```csharp
public UserService : IUserService
{
    private readonly IUserRepository userRepository;

    public UserService(IUserRepository userRepository) // here we let the container resolve the dependency for us
    {   
        this.userRepository = userRepository;
    }
    
    public IEnumerable<User> GetAll()
    {
        // any logic necessary
        return userRepository.GetAll();
    }

    public int CalculateUserAge(Guid id) 
    {
        // any logic
        return CalculatedAge;
    }

    ..
}
```