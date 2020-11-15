# Working with forwarding documents with a workflow

In this code sample we will show how forward a document with a workflow.

## Required Modules

- simplic
  - [DependencyInjection](xref:PythonAPI.DependencyInjection)
- [System](xref:System)
  - [Guid](xref:System.Guid)
- [Simplic.Filestructure.Workflow](xref:Simplic.FileStructure.Workflow)
  - [WorkflowOperation](xref:Simplic.FileStructure.Workflow)
- [Simplic.Session](xref:Simplic.Session.WorkflowOperation)
  - [ISessionService](xref:Simplic.Session.WorkflowOperation)

# Python

```python
from simplic import DependencyInjection
from Simplic.FileStructure.Workflow import IWorkflowOperationService, WorkflowOperation
from Simplic.Session import ISessionService
from System import Guid

# With this script you can put a document in an User-Document-Workflow. Important is the last step: ForwardCopyTo which executes the forwarding process, by adding a file-structure path to the document and adds the document assignment.
def forward_copyTo(self, workflow_id, document_id):

    # Creating an instance of WorkFlowOperation
    model = WorkflowOperation()

    # Getting the Session Service
    sessionService = DependencyInjection.resolve(ISessionService)

    # Changing the WorkflowId to the given parameter workflow_id
    model.WorkflowId = workflow_id

    # Changing the DocumentId to the given parameter document_id
    model.DocumentId = document_id

    # Setting the UserId with the UserId of the current session 
    model.UserId = sessionService.CurrentSession.UserId

    # The TargetUserId is the same as the UserId
    model.TargetUserId = model.UserId

    # The "create" and "update" time is the time at the moment the method is executed
    model.CreateDateTime = DateTime.Now
    model.UpdateDateTime = DateTime.Now

    # Naming the name of the action "forward" and generate a new Guid.
    model.ActionName = "forward"
    model.Guid = Guid.NewGuid() 

    # Getting the Workflow Operation Service
    service = DependencyInjection.resolve(IWorkflowOperationService)

    # Fowards a copy WorkflowOperation to all users that have an instance of the work flow
    service.ForwardCopyTo(model)
```
***

## Expected Output
```

```