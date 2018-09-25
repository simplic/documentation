# Delete statements

Delete statements should be written in the following format:

```sql
DELETE FROM <tablename>
WHERE <column3> = <...>
```

If a joins are required, using alias names is recommended:

```sql
DELETE FROM <tablename> t1
JOIN <tablename2> t2 ON t1.<pk> = t2.<column>
WHERE t1.<column3> = <...> AND t2.<column> = <...>
```