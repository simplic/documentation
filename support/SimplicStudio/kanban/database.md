# Kanban database

All tables that are required for the kanban system starts with `Kanban_`.

## Configuration

All kanban board configurations are store in `Kanban_Configuration`. The pipeline configurations are saved as json in the `Configuration` column.

Sample:

```json
{
	"$id": "1",
	"Id": "11127623-9506-4c87-9866-5ae4fae904e3",
	"InternName": "Standard",
	"DisplayName": "Standard",
	"EnableEdit": true,
	"RefreshInterval": 5,
	"Pipelines": {
		"$id": "2",
		"$values": [
			{
				"$id": "3",
				"Id": "c9ce1581-fdf8-4b5d-945d-eb8a0ca1907e",
				"InternName": "Todo",
				"DisplayName": "kanban_pipeline_todo",
				"MaxItemCount": 0,
				"OrderId": 0
			},
			{
				"$id": "4",
				"Id": "5f805312-4eb4-42b2-b372-7ad4f0cc5cec",
				"InternName": "InProgress",
				"DisplayName": "kanban_pipeline_inprogress",
				"MaxItemCount": 0,
				"OrderId": 1
			},
			{
				"$id": "5",
				"Id": "6d57c4b2-ddff-44c6-9ce7-62e1f23e25e1",
				"InternName": "Failed",
				"DisplayName": "kanban_pipeline_failed",
				"MaxItemCount": 0,
				"OrderId": 2
			},
			{
				"$id": "6",
				"Id": "51a3b33b-ff0b-4de5-b3b7-72c528819fd5",
				"InternName": "Done",
				"DisplayName": "kanban_pipeline_done",
				"MaxItemCount": 0,
				"OrderId": 3
			},
			{
				"$id": "7",
				"Id": "80485c3f-762c-411f-ac9d-ff9b6ee6feaa",
				"InternName": "Done2",
				"DisplayName": "done",
				"MaxItemCount": 0,
				"OrderId": 4
			}
		]
	},
	"CreateDateTime": "2018-10-15T16:40:34.4266827+02:00",
	"CreateUserId": 0,
	"UpdateDateTime": "2018-10-15T16:40:34.4266827+02:00",
	"UpdateUserId": 0,
	"IsGeneric": true
}
```

## Data

All data (tiles) are store in the `Kanban_Data` table.

## Live communication

The `Kanban_Data_Live` table contains data to support the communication between all runnig `Simplic Studio` instances. 