# SQL object and variable naming

## Tables

All tables should be named along the objects they are containig. E.g. the table for storing users must be named `User`. The first
letter must be in upper case. Words within a name should be separated using underscores.

1. Correct: `User`
2. Correct: `Group`
3. Correct: `User_Group_Assignment`
4. Wrong: `UserGroupAssignment`

If a word makes only sense written together, use pascal case:

1. Correct: `GeneralLedgerAccount`
2. Wrong: `General_Ledger_Account`
3. Correct: `GeneralLedgerAccount_Assignment`

If a table contains instancedata, it must start with `IT_`. If a table just contains data which are used as raw import/export table, it must start with `IF_`.

1. `IT_` = InstanceDataTable
2. `IF_` = Interface

### Column names

The base naming convention is pascal case:

1. The first letter must be in upper case
2. Words are continated with an upper latter, **DO NOT** use undescore

Sample:

1. Correct: `FirstName`
2. Correct: `CompanyName`
3. Wrong: `firstName`
4. Wrong: `first_name`

## Procedures

Procedure and function names should start with the main object they are working with. The name must end with the action that procedure or function is doing:

1. Add
2. Delete
3. Get
4. ...

Words within the name should be separated using underscores:

1. Correct: `Notification_Add`

### Parameter names

Parameter must befin with the direction they are dealing with, e.g, `@in_` or `@out_`. The seconds part is the parameter name as camel case, e.g. `@in_user_`.
The last part is a short datatype name: `@in_userName_vc`.

List of short datatype names:

1. varchar = vc
2. integer = int
3. date = date
4. time = time
5. datetime = dt
6. uniqueidentifier = ui
7. numeric = nc
8. bigint = bint
9. long binary = lb

Complete sample: `CREATE OR REPLACE PROCEDURE User_Get(in @in_userId_ui UNIQUEIDENTIFIER) ...`

### Return values

Return value names must follow the rules of table columns.