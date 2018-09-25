# Coding Standards and Naming Conventions

Below are our C# coding standards, naming conventions, and best practices.

We use **PascalCase** for class and method names:

```csharp
public class ClassName
{
    public void MethodName()
    {
        ..
    }    
}
```
We use **camelCase** for method arguments and local variables.

```csharp
public class ClassName
{
    private readonly VariableType variableName;

    public void MethodName(ParameterType parameterName)
    {
        var localVariable = parameterName.MethodName();                
    }
}
```


We use **PascalCase** for constants:
```csharp
public const float ConstantName = 3.14f;
```

We use implicit type **`var`** for variable declarations:
```csharp
var customer = new Customer();
var productManager = new ProductManager();
var pi = 3.14f;
var counter = 0;
```

We ***don't*** use Abbreviations:
```csharp

// Correct
var clientManager = new ClientManager();
var employeeAssignment = new EmployeeAssignment();

// Dont use
var clientMngr = new ClientManager();
var empAssignment = new EmployeeAssignment();

// Exceptions
CustomerId customerId;
XmlDocument xmlDocument;
FtpHelper ftpHelper;
UriPart uriPart;
```

We use **PascalCase** for abbreviations 3 characters or more (2 chars are both uppercase):
```csharp
HtmlHelper htmlHelper;
FtpTransfer ftpTransfer;
UIControl uiControl;
```

We use predefined type names instead of system type names like Int16, Single, UInt64, etc
```csharp
// Correct
string firstName;
int lastIndex;
bool isSaved;
 
// Dont use
String firstName;
Int32 lastIndex;
Boolean isSaved;
```

We prefix interfaces with the letter **I**. Interface names are noun (phrases) or adjectives.
```csharp
public interface IClientRepository { .. }
public interface IProductManager { .. }
```

We check nullables with HasValue method instead of != null. It is clearer to understand what type it is.
```csharp
public Guid? nullableId { get; set; }

// Correct
if (nullableId.HasValue)

// Dont use
if (nullableId != null)
```

**Events and Delegates**

- √ **DO** add the suffix "EventHandler" to names of delegates that are used in events.
- √ **DO** add the suffix "Callback" to names of delegates other than those used as event handlers. 
- X **DO NOT** add the suffix "Delegate" to a delegate.


