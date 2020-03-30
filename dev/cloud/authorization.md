## Authorization

JWT tokens are used for authorization.

There are two set of roles in the system: general system roles and organization-level roles. General roles are Support, Admin, SystemAdmin. Organization roles are BillingManager and Admin.

A user have a set of general roles. Empty set can be seen as a system-wide User role.

A user can belong to many organizations. In each organization he'll have an own set of roles. Empty set can be seen as an organization-level User role.

A common practice is to use authorization policies to access resources. Base WebApi package provides two policies:
- `OrganizationUser`: a user must have a general `Support`, `Admin` or `SystemAdmin` role or an organization `User` (i.e. empty role set) role to access organization resources
- `OrganizationAdmin`: a user must have a general `Support`, `Admin` or `SystemAdmin` role or an organization `Admin` role to access organization resources

Example:
```
"Roles" : [],
"Organizations" : [ 
    {
        "_id" : UUID("c636c93b-8b0b-44b6-ba2e-e61f9955f744"),
        "Roles" : [ 
            0
        ],
        "IsDefault" : true
    }
]
```

A user can create an organization or can be added to it. In the former case he gets `Admin` role in this organization.

If a user doesn't belong to any organization and is added to one, it becomes default to him. This affects login process. The JWT token, generated during login, contains user's general roles and OrganizationId and roles in his default organization, if he has one.

### IOrganizationIdProvider

It's important to restrict access to organization resources for the users of other organizations. In order to do this a few measures applied:
- every DB document (except User) has OrganizationId
- almost all Web API actions require at least OrganizationUser auth policy, which means, OrganizationId value must be provided with every request
- all Get* repository methods (GetById, GetByFilter, GetAll) add filter by OrganizationId by default

In order to get OrganizationId in repository, IOrganizationIdProvider is used. In WebApi projects it's configured to read OrganizationId from HttpContext. It's also used in MassTransit middleware to put OrganizationId in every command, sent from WebApi. Therefore, in Service projects IOrganizationIdProvider is configured to read OrganizationId from command's header.