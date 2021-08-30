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


We use **PascalCase** for `public` constants:
```csharp
public const float ConstantName = 3.14f;
```

and **camelCase** for `private` constants:
```csharp
private const float constantName = 3.14f;
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
### Interfaces
We prefix interfaces with the letter **I**. Interface names are noun (phrases) or adjectives.
```csharp
public interface IClientRepository { .. }
public interface IProductManager { .. }
```
### Nullables
We check nullables with `Nullable<>.HasValue` property instead of `Nullable<> != null`. It is clearer to understand what type it is.
```csharp
public Guid? NullableId { get; set; }

// Correct
if (NullableId.HasValue)
..

// Dont use
if (NullableId != null)
..
```
### Properties and Fields
If you dont do anything else than just assign the value to a field, use auto property instead.

```csharp
// Correct
public string Name { get; set; }

// Dont use
private string name;
public string Name 
{
	get { return name; }
	set { name = value; }
}
```
### Events and Delegates

- √ **DO** add the suffix "EventHandler" to names of delegates that are used in events.
- √ **DO** add the suffix "Callback" to names of delegates other than those used as event handlers. 
- X **DO NOT** add the suffix "Delegate" to a delegate.

### Unused Legacy Code
We don't just comment out old code and commmit it. It is already versioned on git server, so there is no need to comment out old code.
Just remove the old code.

### Linq Expressions
We use method-based LINQ queries:

- √ **DO** `var ids = items.Select(x => x.ExternalId).Cast<decimal>()`.
- X **DO NOT** `var ids = from item in items select (decimal)item.ExternalId`.


### Large Numbers
C# supports the use of an underscore to split down large numbers to an readable format.

- √ **DO** `public const long LargeNumber = 10_000_000_000;`.
- X **DO NOT** `public const long LargeNumber = 10000000000;`.

### Order inside a class
Inside a class the different elements should be ordered as following:
- Fields
- Constructor
- Private-Methods
- Public-Methods
- Properties

```csharp
public class Example
{
  // Field(s)
  private string Field = "Field";

  // Constructor
  public void Example
  {
  }

  // private Method(s)
  private void DoPrivateSomething()
  {
  }

  // public Method(s)
  public void DoPublicSomething()
  {
  }

  // Property/Properties
  public string Property { get; set; }
}
```