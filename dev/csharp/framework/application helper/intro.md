# ApplicationHelper - Interface to the Gridmenu

The applicationhelper is used as an interface to the grid menu configuration. 
Excample:

```csharp
  public static class GridMenuApplicationHelper
 {
      [RequiredFieldInfo("EditGridMenu", new[] { "UI_Grid_Menu_Group.Guid" })]
       public static GridInvokeMethodResult EditGridMenu(GridFunctionParameter parameter)
       {
            if (parameter.SelectedRows.Any())
            {
                var win = new GridMenuGroupWindow();
                var row = parameter.SelectedRows.OfType<ObservableDataRow>().First();
                var group = GridViewManager.Singleton.GetGridMenuGroup((Guid)row["Guid"]);

                win.Edit(group);
                win.Show();

                return new GridInvokeMethodResult()
                {
                    RefreshGrid = true,
                    Window = win
                };
            }
            else
            {
                return null;
            }
        }
	}
```