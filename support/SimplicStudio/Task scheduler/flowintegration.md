# Flow integration

If the scheduler executes a task, it will trigger a flow event. 
The flow event is named `Scheduler started`. The scheduler will execute an event,
if the `Intern name` of the scheduler matches the name in the flow node:

![~/images/Scheduler-Flow.png](~/images/Scheduler-Flow.png)