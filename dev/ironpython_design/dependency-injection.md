# Dependency injection

The simplic python api provides a simple way to resolve services. To resolve a service the `DependencyInjection` package is required:

```python
# Import package
from simplic import DependencyInjection
```

A service can be resovled using the `resolve` method:

```python
# Import package
from simplic import DependencyInjection

# Imorpt service
from Simplic.Authorization import IAuthorizationService

# Resolve instance
service = DependencyInjection.resolve(IAuthorizationService)
service.Migrate()
```

The `resolve` method has one argument, which accepts the type of the interface to resolve.

## Internal method call

The package uses the `CommonServiceLocator` to resolve the interface. The underlying clr-type is passed to the `GetInstance` method of the `ServiceLocator`:

```csharp
public static object resolve(IronPython.Runtime.Types.PythonType type)
{
    return CommonServiceLocator.ServiceLocator.Current.GetInstance(type.__clrtype__());
}
```
