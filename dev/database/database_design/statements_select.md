# Select-Statements

This article contains the rules for select statements:

1. All select statements that returns more than one row, must contain an `ORDER BY`
2. Select statements must be formatted as shown in the following example:

```sql
SELECT
  FirstName
, LastName
FROM UserName
WHERE 1 = 1
ORDER BY FirstName
```

3. All rows must be written in a single line
4. The `,`-separater must be placed in the next/last line
5. `FROM`, `WHERE`, ... must be written in a single line
6. If a column exists in more than one table, an explicit alias must be used:

```sql
SELECT
  -- Use the explicit alias UserId, 
  u.Id as UserId
, g.GroupName
FROM User u
JOIN User_Group ug on ug.UserId = u.Id
JOIN Group g on ug.GroupId = g.Id
```

7. Joins must be written explicit, do not just join using auto-joins over foreign-keys