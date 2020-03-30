## Communication

MassTransit uses RabbitMQ transport to communicate between WebApi and Service and across microservices. In MassTransit there're two types of messages - commands and events. Commands are sent to a single predefined endpoint, while events are received by anyone who listens to them.

In a typical microservice WebApi generate and sends commands on write requests. A  worker Service listens to commands, updates database and emits events. It's possible to configure MassTransit to send all commands, implementing the same interface, to a single endpoint, and this pattern is used extensively. For example, all User-related commands implement IUserCommand. Here's the corresponding MassTransit configuration:
```
configurator.AddRequestClient<IUserCommand>(new Uri($"{rabbitMQSettings.Host}/{Constants.Queues.Service.Command.User}"));
```
Endpoint name consists of RabbitMQ host name and queue name. Queue name is a constant string. The convention is:
```
[microservice name].[consuming application].[message type].[aggregate name]
```
In case of User we have `Account` microservice, user commands will be handled in a `Service` app, message type is `Command` and aggregate name is `User`, so the queue name is:
```
account.service.command.user
```
Worker service implement consumers to process commands/events. By convention we separate command/event consumers even if they process messages for the same aggregate. `Queue` attribute is applied to a consumers to define the queue it reads from. So, User commands get into `account.service.command.user` queue and are processed by `Consumers/Command/UserConsumer.cs`. If Logistics service would listen to User events, it'd have a `Consumers/Event/UserConsumer.cs` for queue `logistics.service.event.user`.

MassTransit provides two options for sending commands - "fire-and-forget" and RPC-style. First option is a bit faster, but we can't know if the command is succeeded. In RPC-style communiсation MassTransit creates temporary queues for responses. This approach is used at the moment.