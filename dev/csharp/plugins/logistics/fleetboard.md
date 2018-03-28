> Please note that this a WIP document. Any feedback is welcome.

# FleetBoard 
FleetBoard is a platform that enables the communication between back-end servers 
and vehicles.

# How does FleetBoard work ?
FleetBoard has SOAP back end. We used their demo client app and extended it a bit.

You can read their docs here: [FleetBoard Docs](https://webservices.fleetboard.com/technical-documentation/services-and-methods.html)

FleetBoard is a flexible communication platform with vehicles. Important things to know are:

- [TMStructure](https://webservices.fleetboard.com/technical-documentation/documents/tmstructure-document.html)
- [TMObjectType](https://webservices.fleetboard.com/technical-documentation/documents/tmobjecttype-document.html)
- [TMObject](https://webservices.fleetboard.com/technical-documentation/documents/tmobject-document.html)
- [FormDef](https://webservices.fleetboard.com/technical-documentation/documents/formdef-document/formdef-document-logistics-service-3rd-generation.html)

You define TMStructures, TMObjectTypes and FormDefs in the back-end. They will be sent to the vehicle using [TransportManagementService](https://webservices.fleetboard.com/technical-documentation/services-and-methods/transportmanagementservice.html)

In order to communicate with a vehicle you need to create a TMObject using the TM service. You need to pass structure id, object type id, vehicle id and form defs as a ```IEnumerable<KeyValuePair<long, string>>```.