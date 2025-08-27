## Database

#### Database name
Database names should __*ALWAYS*__ be lowercase.
Database names are __*FORBIDDEN*__ to contain the following characters:
```
/\. "$*<>:|?
```

The Database name should always include the enviorment 
```
simplic_oxs_staging 
simplic_oxs_production
```
Followed by the name of the service
```
logistics
hr
storage_management
```
Every word should be sepereated by an underline "_ "
Giving a complete name like:
```
simplic_oxs_staging_logistics
simplic_oxs_production_hr
```

In case multiple versions exist of the same service with seperate databases the service version should be added at the end.
```
simplic_oxs_staging_logistics_v3
```


#### Collection name

The collection name should __*ALWAYS*__ be loweercase.
Collection names are __*FORBIDDEN*__ to contain the following characters:
```
$
```

Also collection names cannot start with the "system." prefix or contain ".system."

The collection name should start with the domain the data is in. 
E.g. vehicle for a vehicle domain or tour for the tour domain in the logistics microservice.
```
vehicle
vehcile.type
tour.status
organization.member
```


Instead of CamelCase for a multiple word name we seperate the words by an underline "_ "
```
general_ledger_account.general_ledger_account
workshop_order.status
resource.tractor_unit
```


## Web API 

### Request 
#### Method Usage

##### GET
|                                            |     |     
| ------------------------------------------ | --- | 
| Request has body                           | No  |     
| Successful response has body               | Yes |     
| Safe (Does not change state of the Server) | Yes |     
| Idempontent                                | Yes |     
| Cacheable                                  | Yes |     
A __Get__ Request should always be used when a single resource or an query without a body is used.
Queries with a body should be avoided if possible (with the exception of GQL).

##### POST
|                                            |     |     
| ------------------------------------------ | --- | 
| Request has body                           | Yes |     
| Successful response has body               | Yes |     
| Safe (Does not change state of the Server) | No  |     
| Idempontent                                | No  |     
| Cacheable                                  | No  | 
A __Post__ Request should be used when a resource is added to the microservice.
A Post request can also be used when a resource is get but the query would no longer 
fit in the URL and requires a request body.

##### PUT
|                                            |     |
| ------------------------------------------ | --- |
| Request has body                           | Yes |
| Successful response has body               | May |
| Safe (Does not change state of the Server) | No  |
| Idempontent                                | No  |
| Cacheable                                  | No  |
A __Put__ Request should be used when a resource is replaced to the microservice.

##### PATCH
|                                            |     |     
| ------------------------------------------ | --- | 
| Request has body                           | Yes |     
| Successful response has body               | May |     
| Safe (Does not change state of the Server) | No  |     
| Idempontent                                | Yes |     
| Cacheable                                  | No  | 
A __PATCH__ Request should be used when a resource is parially manipulated in the microservice.

##### DELETE
|                                            |     |     
| ------------------------------------------ | --- | 
| Request has body                           | May |     
| Successful response has body               | May |     
| Safe (Does not change state of the Server) | No  |     
| Idempontent                                | Yes |     
| Cacheable                                  | No  | 
A __DELETE__ Request should be used when a resource is deleted in the microservice.
#### Naming

##### Use lowercase for the entire path
The path and the query parameters should be lowercase and separated by hyphens (`-`) 

DO
```
/appointment
/composed-resource
```

DON'T DO
```
/Appointment
/ComposedResource
```

##### Start with domain context
Request endpoints should always start with the Controllername

DO
```
/geofence/
/loading-aid-type/
```

DON'T DO

```
/post-geofence
/get-loading-aid-type
```

##### Use plural when a list is expected
When a list of responses can be expected the plural should be used.

DO
```
/resources?type=carrier
/tour/{tourId}/loading-slots
```

DONT DO

```
/resource?type=carrier
/tour/{tourId}/loading-slot
```

##### Use nouns instead of verbs
There is no practical reason to include get-by in a request url when it already is a get request.

DO
```
GET /resource/{id} => Get single resource
GET /resources      => Gets all resources
GET /resources/longitude=1.4343.... => Gets all resources at a location
PUT /tour/{tourId}/tour-status/{tourStatusId} => Set status of a tour
POST /tour/preview => gets the preview of a tour after a post request
```

DONT DO
```
GET /resource/get-by-id/{id}
GET /resource/get-all
GET /resource/get-by-location?longitude1.4343....
PUT /tour/set-status
POST /tour/calculate-preview
```

##### One resource one controller
One controller should only respond with one resource. 
This can be partial or aggregated data of a single resource, but not aggregation over all resources.

DO
```
GET /tour/{id} 
GET /tour/{id}/loading-slots
GET /aggregated-loading-slots
```

DONT DO
```
GET /tour/aggregated-loading-slots
```

### Response 

#### Response Code

##### Success Codes

###### Created At Action / 201
The created at action should be returned when a POST request created a new resource.
It should contain the path where the object was created.
It should contain the created object.

###### No Content / 204
No Content should be used when the response body does not contain a body.
E.g. when a resource is deleted. 

###### Success / 200
A Success/200 should always be returned with a body and when no other success status fits.

##### Client Error Codes

###### Bad Request / 400
A bad request should be returned when the request body is not correct.
E.g:
	An Id of a referenced object in the body is not found.
	The mail property does not contain an @

###### Not Found / 404
A not found should be returned when the resource specified in the Url is not found
E.g. /tour/12341234-1234-1234-1234-123412341234 does not exists

#### Response Objects

##### Always
A response should always contain following information of the requested Resource:
	- CreateDateTime
	- CreateUserId
	- CreateUserName
	- UpdateDateTime
	- UpdateUserId
	- UpdateUserName

##### Depended

###### IsDeleted 
Should only be part of the response when a single resource is questioned.
When a list of resources is returned either only deleted are questioned or no deleted should be part of the response.

##### Never

###### OrganiztionId
The OrganizationId should already be known by the client and should not be required to be part of every response.

###### DataExtension of subsets
A subset of an object (e.g. a Shipment in a Tour) should not be required to contain meta information about the subset. This includes information about the create date and time, update user or whether it is deleted.

