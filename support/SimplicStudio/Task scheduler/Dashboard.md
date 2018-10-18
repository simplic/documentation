# Scheduler dashboard

The simplic task scheduler system is basing on ([angfire.io](https://www.hangfire.io/). Hangfire supports a simple dashboard
for task monitoring. The dashboard is available, if the simplic `Web API` is hosted in an application server instance.

> Hint: If you want to start the webservice in a console application, it must be executed in administration context.

The dashboard is available under the following url: `http://<your-configuration>/hangfire`. The default address
must be set in the global configuration section. The setting is named `PublicWebApiBinding` and `PublicWebApiAddress`.

Sample: `http://localhost:58080/hangfire`.

> Hint: In the current version, the web api and scheduler service must be hosted within the same application service instance!