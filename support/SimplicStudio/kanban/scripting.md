# Scripting and API

To add data to a kanban board, the services `IKanbanDataService` and `IKanbanConfigurationService` are required.

Importing services:

```py
from simplic import DependencyInjection
from Simplic.Kanban import IKanbanDataService, IKanbanConfigurationService, KanbanData
from Simplic.DataStack import IStackService

data_service = DependencyInjection.resolve(IKanbanDataService)
configuration_service = DependencyInjection.resolve(IKanbanConfigurationService)
stack_service = DependencyInjection.resolve(IStackService)
```

At first you need to resolve the board and pipeline to add the data to.

```py

kanban_id = configuration_service.GetKanbanIdByName('SampleBoard')
pipeline_id = configuration_service.GetPipelineIdByName('SampleBoard', 'InProgress')
```

Create data and save to database

```py
data = KanbanData()
data.KanbanId = kanban_id
data.PipelineId = pipeline_id
data.Content = 'Sample content, this text can be very large....'
data.Title = 'Title of the data'
data.StackId = stack_service.GetStackId('STACK_Contact')
# data.InstanceDataId = ... Optional instance data guid

data_service.Save(data)
```

If you want to inform the flow system and all running instances within the simplic studio, track the changes:

```py
data_service.TrackChanges(data, True)
```

If the second parameter is set to true, the flow system will be triggered too.

**Result**

![/images/Kanban_API.png](/images/Kanban_API.png)

Setting tile color is possible using the `.Color` option.

```py
data.Color = '#4286f4'
```

Complete script

```py
from simplic import DependencyInjection
from Simplic.Kanban import IKanbanDataService, IKanbanConfigurationService, KanbanData
from Simplic.DataStack import IStackService

data_service = DependencyInjection.resolve(IKanbanDataService)
configuration_service = DependencyInjection.resolve(IKanbanConfigurationService)
stack_service = DependencyInjection.resolve(IStackService)

kanban_id = configuration_service.GetKanbanIdByName('Standard')
pipeline_id = configuration_service.GetPipelineIdByName('Standard', 'InProgress')

data = KanbanData()
data.KanbanId = kanban_id
data.PipelineId = pipeline_id
data.Content = 'Sample content, this text can be very large....'
data.Title = 'Title of the data'
data.StackId = stack_service.GetStackId('STACK_Contact')
# data.InstanceDataId = ... Optional instance data guid
data.Color = '#4286f4'

data_service.Save(data)
data_service.TrackChanges(data, True)
```

# Result

![/images/Kanban_API2.png](/images/Kanban_API2.png)
