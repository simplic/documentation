from simplic import Sql

name = "Lutz"

res = Sql.execute_none_query("insert into testInsertUpdate (Name) values (?)", "default", [name])

res = Sql.execute_none_query("update testInsertUpdate set Name = ? where ID = ?", "default", [name, 2])