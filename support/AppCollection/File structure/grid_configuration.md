# Open file structure editor from instance data grid

This article shows how to open the file structure editor from an instance data grid.

## 1. Prearing the select statement

The select statement of the grid profile has to return the following to columns:

1. `Guid` - Instance data guid
2. `StackGuid` - Id of the stack

**Sample**:

```sql
select
 dc.Guid
, dc.Name
, dc.Number
, dc.StartDate

-- Will be available as const later: , {StackGuid} AS StackGuid
, CAST('7C34528F-7AB0-4BF5-AA86-85760F193106' AS UniqueIdentifier) AS StackGuid
FROM IT_Project dc
[DynamicJoin]
WHERE 1 = 1
[WhereCondition]
AND IsDeleted = 0
ORDER BY dc.Number
```

## 2. Create menu entry

In the second step you need to create a new grid menu entry. The following options must be set:

1. `General -> Displayname`: `project_open_filestructure`
2. `Clr/.Net -> Class`:  `ApplicationHelper`
3. `Clr/.Net -> Namespace`:  `Simplic.FileStructure.UI.Helper`
4. `Clr/.Net -> Method`: `OpenFileStructureEditor`
5. `Design -> Large icon`: `file_structure_template_32x` 
6. `Design -> Small icon`: `file_structure_template_32x`
7. `Design -> Button size`: `Large`