# Navigation commands

Navigation commands allow to navigate within the simplic framework by typing in a command. Commands
can be simple shortcuts, application names or even generic commands, like starting a call.

![~/images/navigation_command_sample.png](~/images/navigation_command_sample.png)

A command has the following properties:

 1. Unique id
 2. Name
 4. Shortcut/command
 5. Icon
 6. Has a parameter

The command consists of two services:

1. `INavigationCommandService`: Stores commands and contains the event to catch executed commands
2. `INavigationCommandSearchService`: Allows to search for a command by a command line input (string)

## Command input

The search algorithm lists the commands in the following order:

1. The input matches a command/shortcut
2. A command name starts with the input string and has no parameter
3. A command name starts with the input string and has a parameter

The 2nd and 3rd might switch if a command requires parameters or not.

If a command contains multiple words within the name, the search engine splits the words by the space character.
This allows to just type at the beginning of any word.

Parameter must be separated by using a space character from the command. Take a look at the phone call sample at the bottom.

## Examples

* `cmd` will start the simplic python command line interface (command/shortcut)
* `console` will start the simplic python command line interface (full command name)
* `docm` will start the simplic document management application (command/shortcut)
* `# 05121206850` will start a call to `05121206850` (command/shortcut with parameter)
 