## Web Api

Each WebApi project references Simplic.Cloud.WebApi package and use its base classes (BaseProgram, WebApiBootstrap, BaseController) to enable consistent behavior across all WebApi projects. This includes:
- Serilog logging
- authentication
- authorization
- CORS configuration
- DB context initialization
- MassTransit initialization
- Automapper configuration
- action naming convention
- consistent BadRequest responses format
- Swagger configuration
- OrganizationId provider