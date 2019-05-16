# Order shipment in tour window

Changing the shipment order in a tour is only allowed, if the db-field `IT_Tour.SetTourStartEndContactAutomatically` is set to `1`.
The default value of the field can be set using the global setting `logistics/TourStartEnd`. Changing the global settings, *will not*
affect older tour entries.