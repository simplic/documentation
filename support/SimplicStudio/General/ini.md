# Ini file

The simplic ini file is located under `your-installation-path\Simplic Studio\Configuration\Studio.ini`. The ini file is separated
into different section. To use a section you can either start simplic with the `--section <name>` argument or use the login dialog
for selecting a section.

The following options are available withing a section:

| Key                  | Description                                                       | Sample                                               | Default value |
|----------------------|-------------------------------------------------------------------|------------------------------------------------------|---------------|
| UserConnectionString | Connection string without uid and pwd                             | server=simplic;dbn=simplic;charset=utf-8;links=TCPIP |               |
| SectionFriendlyName  | Friendly name for the login dialog                                |                                                      |               |
| IsHiddenSection      | If set to 1, the section will not  be visible in the login dialog |                                                      | 0             |
| ConnectionString     | Connection string with uid and pwd. Depricated!                   |                                                      |               |