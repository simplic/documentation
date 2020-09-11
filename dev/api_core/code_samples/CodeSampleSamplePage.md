# Working with CostCenters

In this code sample we will show how to instantiate and save CostCenters.

## Required Modules

- [Simplic.ERP.Core](xref:RefTest)
  - [CostCenter](xref:RefTest.Contact)
  - [CostCenterManager](xref:RefTest.ContactCollection)

## Samples

# [C#](#tab/tabcsharp)

```csharp
using Simplic.ERP.Core;
using System;

namespace CodeSample
{
    CostCenter costCenter = new CostCenter();
    costCenter.Guid = Guid.NewGuid();
    costCenter.IsDistributed = true;
    costCenter.IsError = false;
    costCenter.Name = "Sample CostCenter";
    costCenter.Number = 1;
    costCenter.TypeId = 1;
    costCenter.TenantId = Guid.Parse("00000000-0000-0000-0000-000000000002");

    var currentDate = DateTime.Now;
    var time = new TimeSpan(24, 0, 0);

    costCenter.ValidFrom = currentDate;
    costCenter.ValidTo = currentDate.Add(time);

    var costCenterManager = new CostCenterManager();
    costCenterManager.Save(costCenter);
}
```

# [Python](#tab/tabpython)

```python
from Simplic.ERP.Core import CostCenter, CostCenterManager
from System import Guid, DateTime, TimeSpan

cost_center = CostCenter()
cost_center.Guid = Guid.NewGuid()
...
cost_center_manager = CostCenterManager()
cost_center_manager.Save(cost_center)
```
***

## Expected Output
```
```
