# Grid integration

The option to put data into a kanban is available in all instance data grids. If the user select the menu option, all 
kanban boards with the setting `is generic` enabled will be shown.

By doubleclicking on a pipeline, the data will be added to the board. The kanban system reacts to the following selected grid columns.
The columns are optional. If the columns are set, the default values will be ignored.

* `KanbanContent` - Sets the content of the tile (data item). If not set, the friendly name of the instance data will be used
* `KanbanTitle` - Sets the title of the tile. If not set, the stack name will be used
* `BlobGuid` - If set, the blob guid will be passed to the tile. By clicking the tile, the document will be shown in the document viewer
* `FileExtension` - Contains the file extension of the passed blob guid. This column is required to show a document in the document viewer