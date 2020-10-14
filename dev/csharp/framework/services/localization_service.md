# Localization Service

**Note:** we use Simplic.Localization (Simplic nuget package)

## What is it ?
Returns string automatically in the right language. Use when text needs to be displayed to the user of the program.

## How to use it ?
First, search for [SOMETHING][LANGUAGE_ABBREVIATION].json -> i. e. DE.json -> fullFileName: global.de-DE.json
Currently only DE and US Languages are supported.
Add in eacht localization-file the KEY and YOUR STRING translated in localizationflile language
**Note:** The key for the same string translated into different languages is required to be the same

i. e. "federal_state_required":  "Das Bundesland muss angegeben werden."

Then, go to c# and get the string through the key as follows
```csharp
using Simplic.Localization;

public class myClass
    {
        private readonly ILocalizationService localizationService = CommonServiceLocator.ServiceLocator.Current.GetInstance<ILocalizationService>();

        public void MyMethod()
        {
            Console.WriteLine(localizationService.Translate("your_Key"));
        }
    }
```
