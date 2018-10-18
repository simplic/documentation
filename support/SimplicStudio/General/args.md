# Application arguments

This article is about the arguments which are available in the `Simplic Studio.exe` and `ApplicationServer.exe`.

## Simplic Studio.exe and ApplicationServer.exe

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--section` | Section/database from ini file to start the application with                             | `--section sample` |

## Simplic Studio.exe only

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--touch` | Touch screen optimzation                            | `--touch` |
| `--nocache` | Disables the cache system                            | `--nocache` |
| `--username` | Default username for login process. Will be used for pass trhough too.                            | `--username sample` |
| `--password` | default password for login process. Will be used for pass trhough too.                            | `--password mypassword123` |
| `--passthrough` | Disables the cache system                            | `--passthrough` |

## ApplicationServer.exe only

| Argument                  | Description                                                       | Sample                                               |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|
| `--name` | Name of the application server                             | `--name sample_server` |
| `--install` | Installs the application server as windows service                             | `--install` |