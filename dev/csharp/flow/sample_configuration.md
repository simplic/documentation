# Sample Flow Configuration File
```json
{
    "Id": "a9bce7af-33ba-4a71-b3d9-9eaf8c619329",
    "Name": "Workflow name comes here",
    "Nodes": [
        {
            "Id": "41a50134-aadd-4d30-99dc-34f42d88d241",
            "NodeType": "EventNode",
            "ClassName": "OnCheckDirectoryContentNode",
            "IsStartEvent": true,
            "Pins": [],
            "PositionX": 240,
            "PositionY": 220,
            "Width": 200,
            "Height": 150
        },
        {
            "Id": "3d673de0-7a63-4ddf-a515-0e71eb624d10",
            "NodeType": "ActionNode",
            "ClassName": "ConsoleWriteLineNode",
            "IsStartEvent": false,
            "Pins": [
                {
                    "Name": "InPinToPrint",
                    "DefaultValue": "This is a default value"
                }
            ],
            "PositionX": 560,
            "PositionY": 220,
            "Width": 200,
            "Height": 150
        },
        {
            "Id": "4a5dd3c4-5085-4665-b4b2-eeb1d7bdce78",
            "NodeType": "ActionNode",
            "ClassName": "ConsoleWriteLineNode",
            "IsStartEvent": false,
            "Pins": [],
            "PositionX": 860,
            "PositionY": 220,
            "Width": 200,
            "Height": 150
        }
    ],
    "Links": [
        {
            "From": {
                "NodeId": "41a50134-aadd-4d30-99dc-34f42d88d241",
                "PinName": "OutNode"
            },
            "To": {
                "NodeId": "3d673de0-7a63-4ddf-a515-0e71eb624d10",
                "PinName": "FlowIn"
            }
        },
        {
            "From": {
                "NodeId": "3d673de0-7a63-4ddf-a515-0e71eb624d10",
                "PinName": "OutNode"
            },
            "To": {
                "NodeId": "4a5dd3c4-5085-4665-b4b2-eeb1d7bdce78",
                "PinName": "FlowIn"
            }
        }
    ],
    "Pins": [
        {
            "From": {
                "NodeId": "41a50134-aadd-4d30-99dc-34f42d88d241",
                "PinName": "OutPinDirectoryPath"
            },
            "To": {
                "NodeId": "4a5dd3c4-5085-4665-b4b2-eeb1d7bdce78",
                "PinName": "InPinToPrint"
            }
        }
    ]
}
```