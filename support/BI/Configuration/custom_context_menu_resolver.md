# Custom context menu entry resolver/service

To create a custom context menu resolver, it is required to create a custom service and register it.
Everything in this sample is done in the `main.py` in the `/private/` directory.

```python
from simplic import DependencyInjection
from Simplic.BusinessIntelligence import IBusinessIntelligenceContextMenuResolver
from System.Windows import MessageBox

class SampleContextMenuService(IBusinessIntelligenceContextMenuResolver):

	def Open(self, configuration, key, parameter):
		# configuration: Contains the full configuration object
		# key: The key from the context menu configuration
		# parametr: The selected row as dictionary. The keys are the same as in the underlying view.

		# Show value
		MessageBox.Show('Selected shipment: ' + str(parameter[key]))

DependencyInjection.register_instance(IBusinessIntelligenceContextMenuResolver, "BISampleContextMenu", SampleContextMenuService())
```

The context menu can be registered this way in the configuration file. The `service` name must be the same as in te `register_instance` code line.

```json
{
	"displayName": "Sample ",
    "key": "ShipmentNr",
    "service": "BISampleContextMenu"
}
```