# Hirachical grid

Using hierarchical grids, information can be displayed nested. 

![~/images/hierarchical_grid_sample.png](~/images/hierarchical_grid_sample.png)

To mark a grid as a hierarchical grid, the following steps are necessary:

**Parameter definition**

For hierarchical grids to work, the parameter to be passed to the nested grid must be defined at the beginning. The parameter column must be the first column in the select statement:

```
select
  dc.ContactId as OrganizationContactId
ContactId.
t.c.guide
, dc.Additional01
, dc.Birthday
, dc.BusinessHomePage
....
```

**Create a hierarchical grid**

At the beginning a Simplic-Grid must be created. The grid can access the parameter of the overlying grid. The syntax for this is: `:<Name>'. Example: `:OrganizationContactId`.

A complete statement looks like this:

```
select
  dc.Guid
ContactId.
, dc.Birthday
, dc.BusinessHomePage

-- ....
-- ....
-- ....
-- ....

where 1 = 1
AND ISNULL(dc.IsDeleted, 0) = 0
and dc.ContactIDRef = :OrganizationContactId

ORDER BY dc.CompanyName, dc.LastName, dc.FirstName
```

If the parameter is stored in the statement, the configuration is complete.

**Connecting grids**

The nested grid must be set in the main grid. This is done in the "Hierarchical Grid" tab. In addition, the checkbox "Use Hierarchical Grid" must be checked.

![~/images/nested_grid.png](~/images/nested_grid.png)

Afterwards the configuration is finished.