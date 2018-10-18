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
| `--no-plugins` | no plugins will be loaded                            | `--no-plugins` |

## ApplicationServer.exe only

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--name <service-name>` | Name of the application server                             | `--name sample_server` |
| `--install` | Installs the application server as windows service                             | `--install` |
| `--uninstall` | Uninstalls the application server as windows service                             | `--install` |

### Sample

* Login with pass through: `"Simplic Studio.exe" --username sample_user --password mypassword --passthrough`
* Install application server: `ApplicationServer.exe --name FlowService --install`