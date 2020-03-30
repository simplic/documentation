## Service

Each Service project references Simplic.Cloud.Service package and use its base classes (BaseProgram, BaseWorkerService) to enable consistent behavior across all Service projects. This includes:

- Serilog logging
- DB context initialization
- MassTransit initialization
- Redis initialization
- Automapper configuration
- OrganizationId provider
- consistent Command responses format
- appSettings initialization