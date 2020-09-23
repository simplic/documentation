# Working with Dependency Injection

In this code sample we will show an easy way to resolve services. 
## Required Modules

- simplic
  - [DependencyInjection](xref:PythonAPI.DependencyInjection)
- [Simplic.Authorization](xref:Simplic.Authorization)
  - [IAuthorizationService](xref:Simplic.Authorization.IAuthorizationService)

## Samples

# Python

```python
from simplic import DependencyInjection
from Simplic.Authorization import IAuthorizationService

# Resolve instance. The resolve method has one argument, which accepts the type of the interface to resolve.
service = DependencyInjection.resolve(IAuthorizationService)
service.Migrate()
```
***

## Internal method call
```csharp
// The package uses the CommonServiceLocator to resolve the interface. The underlying clr-type is passed to the GetInstance method of the ServiceLocator:
public static object resolve(IronPython.Runtime.Types.PythonType type)
{
    return CommonServiceLocator.ServiceLocator.Current.GetInstance(type.__clrtype__());
}
```
