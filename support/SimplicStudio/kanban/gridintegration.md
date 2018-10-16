# Grid integration

The option to put data into a kanban is available in all instance data grids. If the user select the menu option, all 
kanban boards with the setting `is generic` enabled will be shown.

By doubleclicking a on a pipeline, the data will be added to the board. The kanban systems reacts on the following selected grid columns.
The columns are optional. If the columns are set, the default values will be ignore.

* KanbanContent - Sets the content of the tile (data item). If not set, the friendly name of the instance data will be used
* KanbanTitle - Set the title of the tile. If not set, the stack name will be used
* BlobGuid - If set, the blob guid will be passed to the tile, and the viewer will be activated in the board
* FileExtension - If set, the file extension will be passed to the tile, and the viewer will be activated in the board