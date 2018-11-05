# Frontend localization

The simplic frontend localization is based on a list of json files that are stored in the simplic repository (database). All product (standard) localization files are located under: `/public/Localization`. All files have the following naming convention: `<plugin-name>.<language>.json`. E.g. `logistics.de-DE.json`. The language contains
language and culture information.

## Loading localization information

The localization information gets loaded when the application is started. If a key is located in more than one file, the last key-value will override the previous values.
A localization file looks like this:

```json
{
	"key": "value",
	"label_firstname": "Firstname",
	// ....
}
```

## Customizing

To customize the localizations, a localization file must be placed under: `/private/Localization`. The file must follow the naming conventions above. Since the private localization files will be loaded after the public files, the key-value pairs will be override the public key-values.