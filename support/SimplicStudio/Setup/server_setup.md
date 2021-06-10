# Server setup

To install a new Simplic Studio instance, follow these steps:

# Requirements

The following requirements must be set up for a Simplic Studio instance.

## Redis

Redis is used for caching in the simplic software architecture.

### Windows

**It is recommended to use Redis on Linux**

Download and install the latest setup from https://github.com/microsoftarchive/redis/releases

Use the msi-setup if you want to install redis as a service. If you are downloading the zip-version, it just needs to be unpacked.
This is just for testing and development purpose, not for using it in a productive environment.

After unpacking the zip-file, start `redis-server.exe`. When installing redis as a service, it can be started using the windows service management.

### Linux

TDB

## RabbitMQ

RabbitMQ is used as a message broker to send messages between services to ensure scalability.

### Windows

For installing RabbitMQ on a windows machine, please follow these [instructions](https://www.rabbitmq.com/install-windows.html).

It is recommended to install the [RabbitMQ dashboard](https://www.rabbitmq.com/management.html) as well.

Using the follwoing steps, the management plugin can be installed:

1. Navigate to using cmd `C:\Program Files\RabbitMQ Server\rabbitmq_server-3.8.2\sbin` (depending on your RMQ version)
2. Activate the plugin using the command: `rabbitmq-plugins enable rabbitmq_management` (Use admin previliges)

After logging into the management plugin using `http://localhost:15672/` (username `guest` password `guest`)

Create a new user with the required rigths and allow to connect from all origins.

If the Simplic Studio instance runs on multiple machines in a network, the [ip-binding](https://www.rabbitmq.com/networking.html#interfaces) needs to be configurated.

### Linux

TDB

## Sybase Sql Anywhere

### Windows

**For developing purpose only**

Download and the sybase 17 developer package [Sybase SAP Sql Anywhere 17](https://www.sqlanywhere.info/EN/sql-anywhere/try-sql-anywhere-source_adwsqla2.html)
Ensure that the following components are installed:

* Sybase Central (Administrative Tools)
* ODBC-Driver (x86 and x64)
* Network and Personal Server

### Linux

TDB

# Simplic Studio Setup

## Setup

Download the latest Simplic Studio setup from the [Simplic Developer Network](http://dn.simplic.biz)

## Setup new database

