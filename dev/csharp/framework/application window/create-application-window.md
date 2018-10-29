# Main application window

The simplic framework allows different main windows. The main window is selectable using the application arguments `--app`. E.g. `--app simplic-studio`. This will start
the simplic default application window.

## Creating a new application window

**Required nuget packages:** Simplic.Studio.UI

All application window must inherit from two class:

* `Simplic.Studio.UI.IMainWindow`
* `System.Windows.Window`

The new main window must be registered in the unity container:

```csharp
var container = // ... get cotnainer

container.RegisterType<IMainWindow, MainWindow>("simplic-studio", new ContainerControlledLifetimeManager());
```

All main windows must be registered with a name. The name will be used in the arguments. The `ContainerControlledLifetimeManager` must be used, to not create
new instances when resolving the main window by using `container.Resolve<IMainWindow>("simplic-studio")`.

## Sample

```csharp
public partial class SampleWindow : IMainWindow, Window
{
	// ....
}
```

**Registration**

```csharp
container.RegisterType<IMainWindow, SampleWindow>("sample", new ContainerControlledLifetimeManager());
```

**Starting the application:** `--app sample`