# Update statements

Update statements should be written in the following format:

```sql
UPDATE <tablename>
SET <column1> = 'value'
, <column2> = 'value'
WHERE <column3> = <...>
```

If a joins are required, using alias names is recommended:

```sql
UPDATE <tablename> t1
JOIN <tablename2> t2 ON t1.<pk> = t2.<column>
SET t1.<column1> = 'value'
, t1.<column2> = 'value'
WHERE t1.<column3> = <...>
```