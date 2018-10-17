# Geocoding

To enable geocoding, the simplic application server module `Calculate GeoCoordinates` must be activated. The geocoordinates are stored in `IT_Contacts_PhysicalAddress`. Geocoordinates will be calculated if `GeoCoordinateStatus` is `0` and `CalculateGeoCoordinates` is `1`. 

Values of `GeoCoordinateStatus`:

* 0 - not calculated yet
* 99 - failed
* 100 - successful

Geocoordnates can be recalculated using the simplic contact application. The geocoding process will also be started, of a contact is saved.

## Refresh using python

To refresh geocoordinates for a single contact, the following python api can be used:

```python
# Import 
from sac import ContactManagement

# Contact guid from IT_Contacts
contact_guid = ...

# Calculated 
ContactManagement.update_geo_coordinates(contact_guid)

```