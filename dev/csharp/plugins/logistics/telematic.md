> Please note that this a WIP document. Any feedback is welcome.

# Telematic
- [FleetBoard](fleetboard.md)

# How does Simplic.Telematic work ?

In order to have a flexible system allowing different providers we have developed a couple of concepts.
We queue information that has to be sent to the vehicle, a background service processes these. The background service reads the queue item and decides which provider, which context and which function (python script) to use. It then runs the python script and uses providers methods to finish the job.


Lets start with how data is saved.

**Telematic System**

This is the most basic table we have. It just tells us which provider we are gonna use.
E.g.: FleetBoard
```SQL
CREATE TABLE "IT_Telematic_System" (
	"Guid" UNIQUEIDENTIFIER NOT NULL UNIQUE,
	"Name" VARCHAR(100) NOT NULL,
	PRIMARY KEY ( "Guid" ASC )
) IN "system";
```


**Telematic Context**

This table saves the information about what is the context of the data we would like to send to the vehicle. This part is important. You ll understand soon.
```SQL
CREATE TABLE "IT_Telematic_Context" (
	"Guid" UNIQUEIDENTIFIER NOT NULL UNIQUE,
	"Name" VARCHAR(100) NOT NULL,
	PRIMARY KEY ( "Guid" ASC )
) IN "system";
```

**Telematic Function**

This table is the most complicated one. It has context, system and python script information. These will be used to decide which telematic provider to use, which context to get the data out of and which python script to call.

```SQL
CREATE TABLE "IT_Telematic_Function" (
	"Guid" UNIQUEIDENTIFIER NOT NULL UNIQUE,
	"DisplayName" VARCHAR(100) NOT NULL,
	"InternalName" VARCHAR(100) NOT NULL,
	"ContextId" UNIQUEIDENTIFIER NOT NULL,
	"SystemId" UNIQUEIDENTIFIER NOT NULL,
	"HandlerPath" VARCHAR(1000) NULL,
	"DlrClassName" VARCHAR(100) NULL,
	"IconId" UNIQUEIDENTIFIER NULL,
	"OrderNumber" INTEGER NULL DEFAULT 0,
	"ResolverName" VARCHAR(100) NULL,
	"RequiresVehicle" BIT NOT NULL DEFAULT 1,
	PRIMARY KEY ( "Guid" ASC )
) IN "system";
```

**Telematic Queue**

This is the table where the actual queue item is saved. It has all the necessary information to communicate with a vehicle. 

```SQL
CREATE TABLE "IT_Telematic_Queue" (
	"Guid" UNIQUEIDENTIFIER NOT NULL UNIQUE,
	"FunctionId" UNIQUEIDENTIFIER NOT NULL,
	"ContextDataId" UNIQUEIDENTIFIER NOT NULL,
	"Status" TINYINT NOT NULL DEFAULT '0',
	"PayLoad" LONG BINARY NULL,
	"CreateTime" "datetime" NULL DEFAULT CURRENT TIMESTAMP,
	"UpdateTime" "datetime" NULL,
	"VehicleId" UNIQUEIDENTIFIER NULL,
	PRIMARY KEY ( "Guid" ASC )
) IN "system";
```

# System Resolver
System resolver classes are basically system providers. System Resolver types need to be registered to the unity container with a name ending with "SystemResolver" (Take a look at [Dependency Injection](../../dependency_injection.md)).

**Example:**
```csharp
container.RegisterType<ITelematicSystem, FleetBoardResolver>("FleetBoardSystemResolver");
```

Must implement `Simplic.Telematic.Core.ITelematicSystem` interface.

Check [FleetBoard System Resolver](fleetboard.md) for an example.

# Context Resolver

Context resolver is used to get data from simplic studio. Also needs to be registered to the container with the name ending with "ContextResolver".

Must implement `Simplic.Telematic.Core.ITelematicContext`

**Example:**
```csharp
container.RegisterType<ITelematicContext, ShipmentContextResolver>("ShipmentContextResolver");
```

# Function Resolver

Function resolver is used to do the actual work. Needs to be registered to the container with a name ending with "FunctionResolver".

Must implement `Simplic.Telematic.Core.ITelematicFunction`

**Example:**
```csharp
container.RegisterType<ITelematicFunction, InputBoxResolver>("InputBoxFunctionResolver");
```

In this example above, the function resolver requires users to enter a text to be sent to the vehicle. 

As you can see the possibilities are endless with this system.



