# Task scheduler

The simplic task scheduler allows you to execute task with a given time schedule. The scheduler can be configurated
under the **Configuration** section. 

> Hint: Only active scheduler will be executed.

When configuration a scheduler, the `Windows-Server` and `App-Server` are two important options. The scheduler system will only execute tasks,
if the server name and app-server-name are matching with the currently hosting simplic application server.

## Modes

A task is divided into two modes:

* `Seconds`
* `Cron`

If the `Seconds` mode is selected, the task will be executed in the given interval. The smallest value is 10 seconds. If the `Cron` mode is selected,
you can schedule a task by using the linux cron-job syntax.

### Cron sample:

* Execute a task every minute: `*/1 * * * *`
* Execute a task every hour at half past hour: `30 */1 * * *`. E.g.: *01:30*, *02:30*, ...

Some more examples are available [here](https://www.stetic.com/developer/cronjob-linux-tutorial-und-crontab-syntax.html) and [here](https://wiki.ubuntuusers.de/Cron/).

