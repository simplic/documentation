# Add new command

Commands must be added by using the navigation command service: 

```csharp
var navigationCommand = ServiceLocator.Current.GetInstance<INavigationCommandService>();
```

> This example use the `CommonServiceLocator`. It is recommended to resolve services using a constructor.

To add a new command, an instance of `NavigationCommand` must be created and added:

```csharp
var callCommandId = Guid.Parse("0f25c4e1-c505-4efc-b1c3-54b3524c5ed3");
var phoneIconId = Guid.Parse("E1FCFE21-5F2F-4836-AB33-C07EE4DAD9F7");

navigationCommand.AddCommand(new NavigationCommand
{
    Command = "#",
    Name = localizationService.Translate("start_phone_call"),
    Id = callCommandId,
    HasArguments = true,
    IconId = phoneIconId
});
```

Now the command is available

## Execute command

If a command is executed, the `ExecuteCommand` of the service will be invoked. The following
examples shows how to handle the execution:

```
// Handle commands
navigationCommand.ExecuteCommand += (s, e) =>
{
    // Check whether the phone call command is executed
    if (e.Command.Id == callCommandId)
    {
        // Check whether exactly one arguments exists
        if (e.Arguments.Count != 1)
        {
            // If there is more or less than one argument, return a failed state
            e.Result.ExecutionFailed = true;

            // Set error message
            e.Result.ErrorMessage = localizationService.Translate("navigation_command_call_wrong_parameter");
            return;
        }

        if (!Framework.PhoneInterface.PhoneController.Singleton.IsActive)
        {
            e.Result.ExecutionFailed = true;
            e.Result.ErrorMessage = localizationService.Translate("navigation_command_tapi_inactive");
            return;
        }

        try
        {
            // Try to start a phone call
            Framework.PhoneInterface.PhoneController.Singleton.Interface.Call(e.Arguments[0], Guid.Empty);
        }
        catch (Exception ex)
        {
            // In case of an exception, set the execution as failed
            e.Result.ExecutionFailed = true;
            e.Result.ErrorMessage = localizationService.Translate("navigation_command_tapi_failed", ex.Message);
        }
    }
};
```

> It is recommended to catch the exceptions in the event handler, to return specific error messages.
> Error messages will be handled by the `ExecutionFailed` event.