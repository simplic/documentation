# Set input field as required

**Note:** we use Simplic.UI.MVC

## What is it ?
It blocks any saving action made by the user if required fields are not filled properly

## How to use it ?
Go to the place where a new object of the viewmodel of your window is beeing created and returned
Add Validators before returning the object

i. e.

```csharp
            var viewModel = new YourViewModel(SOMETHING);
            viewModel.AddValidator("NameOfPropertyThatShouldNotBeEmpty", new PropertyGuidEmptyValidator()); //choose best fitting Validators
            viewModel.AddValidator("NameOfPropertyThatShouldNotBeEmpty", new PropertyNotNullValidator());
            return viewModel;
```
