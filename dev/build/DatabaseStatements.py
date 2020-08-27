import sqlalchemy
import urllib
import pyodbc

def fetch_procedures(cursor):
    cursor.execute("Select proc_name, remarks from sys.sysprocedure where creator = 101 and remarks like '<module>%' order by proc_name asc")
    return cursor.fetchall()

def fetch_tables(cursor):
    cursor.execute("select "
                    + "t.table_name,"
                    + "c.cname,"
                    + "c.coltype,"
                    + "c.nulls,"
                    + "c.length,"
                    + "c.syslength,"
                    + "c.in_primary_key,"
                    + "c.colno,"
                    + "c.default_value,"
                    + "c.column_kind,"
                    + "t.remarks as table_remarks,"
                    + "c.remarks as column_remarks,"
                    + "primary_tname as foreign_key_origin,"
                    + "column_name_primary as foreign_key_origin_name,"
                    + "tm.remarks as foreign_key_origin_remarks "
                    + "from sys.systable as t "
                    + "join "
                    + "sys.syscolumns as c on c.tname = t.table_name "
                    + "left outer join "
                    + "(select "
                    + "foreign_tname,"
                    + "primary_tname,"
                    + "substring(columns, 0, charindex(' IS ', columns)) as column_name_foreign,"
                    + "substring(columns, charindex(' IS ', columns) + 4, length(columns)) as column_name_primary "
                    + "from sys.sysforeignkeys) as f "
                    + "on t.table_name = f.foreign_tname and c.cname = f.column_name_foreign "
                    + "left outer join sys.systable as tm "
                    + "on foreign_key_origin = tm.table_name "
                    + "where t.table_type = 'BASE' and t.creator = 101 and t.remarks like '<module>%' "
                    + "order by t.table_name asc, c.colno asc")
    return cursor.fetchall()

def fetch_views(cursor):
    cursor.execute("select "
                    + "t.table_name,"
                    + "c.cname,"
                    + "c.coltype,"
                    + "c.nulls,"
                    + "c.length,"
                    + "c.syslength,"
                    + "c.in_primary_key,"
                    + "c.colno,"
                    + "c.default_value,"
                    + "c.column_kind,"
                    + "t.remarks as table_remarks "
                    + "from sys.systable as t "
                    + "join "
                    + "sys.syscolumns as c on c.tname = t.table_name "
                    + "where t.table_type = 'VIEW' and t.creator = 101 and t.remarks like '<module>%' "
                    + "order by t.table_name asc, c.colno asc")
    return cursor.fetchall()

if __name__ == '__main__':
    conn = pyodbc.connect('DRIVER={SQL Anywhere 12};SERVER=sc-dev02;LINKS=tcpip;DATABASE=simplic;UID=admin;PWD=school;')
    cur = conn.cursor()