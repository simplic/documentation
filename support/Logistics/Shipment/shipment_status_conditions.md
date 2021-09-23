# Shipment Status Conditions
The shipment status depends on several conditions.\
When the status is resolved the service will get all available statuses from the database and tries to resolve them ordered descending of the order number.\
The first matching status is chosen.\
The listed status are orderd in the order they will be given to the customer by default.

## Billing canceled
This status will be set when either the shipment is deleted or the last transaction is a cancellation transaction.\
Other names for this status are:
- Storniert

## Billed
This status will be set when all shipment billable shipment items have a billable status and the last transaction where the shipment is part of is not a cancellation transaction.\
Other names for this status are:
- Abgerechnet

## Reported
This status will be set when all billable shipment items have a billed status.\
Other names for this status are:
- Rückmeldung
  
## Document sent
This status will be set when the shipment has a connected document.
Other names for this status are:
- TA-Versandt

## Scheduled
This status will be set when the shipment is placed on a tour.\
Other names for this status are:
- Disponiert

## Preplanned
This status will be set when the shipment is part of a preplanned tour.\
Other names for this status are:
- Vorgeplant

## New
This is the default status which will be set when the shipment in not part of any tour.\
Other names for this status are:
- Erfasst
