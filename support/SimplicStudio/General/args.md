# Application arguments

This article is about the arguments which are available in the `Simplic Studio.exe` and `ApplicationServer.exe`.

## Simplic Studio.exe and ApplicationServer.exe

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--section <section-name>` | Section/database from the ini file to start the application with                             | `--section sample` |
| `--debug-area <debug-area1;debug-area-2>` | Enables loggin for the given debug areas                             | `--debug-area sql;tapi` |

## Simplic Studio.exe only

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--touch` | Touch screen optimization                            | `--touch` |
| `--nocache` | Disables the cache system                            | `--nocache` |
| `--username <username>` | Default username for login process. Will be used for pass through too.                          | `--username sample` |
| `--password <password>` | default password for login process. Will be used for pass through too                            | `--password mypassword123` |
| `--passthrough` | Tries to execute the login process by using the information from `--username` and `--password`.                            | `--passthrough` |
| `--localization <language>` | Overrides the default localization                            | `--localization de` |
| `--no-plugins` | No plugins will be loaded                            | `--no-plugins` |
| `--app` | Defines the application main window that should be shown after the login. Default is `simplic-studio`                            | `--app simplic-studio` |

## ApplicationServer.exe only

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--name <service-name>` | Name of the application server                             | `--name sample_server` |
| `--install` | Installs the application server as windows service                             | `--install` |
| `--uninstall` | Uninstalls the application server as windows service                             | `--install` |


## Simplic.Archive.exe

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `<document-id>` | Saves the blob in the file-system and opens it in the connected application. (Uses default section) | `3a7b7d34-a5f0-4b0a-b85a-0e8a576408dc` |
| `<section> <document-id>` | Saves the blob in the file-system and opens it in the connected application. Using a specific section. | `sample_section 3a7b7d34-a5f0-4b0a-b85a-0e8a576408dc` |
| `<section> <ArchiveConnectionName> <document-id>` | Saves the blob in the file-system and opens it in the connected application. Using a specific section and connection name for the archive db | `sample_section DatevSqlArchive 3a7b7d34-a5f0-4b0a-b85a-0e8a576408dc` |

### Sample

* Login with pass through: `"Simplic Studio.exe" --username sample_user --password mypassword --passthrough`
* Install application server: `ApplicationServer.exe --name FlowService --install`