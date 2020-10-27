import sqlalchemy
import urllib
import pyodbc

def fetch_procedures(cursor):
    # cursor.execute("Select proc_name, remarks from sys.sysprocedure where creator = 101 and proc_defn like 'create procedure%' and remarks like '<module>%' order by proc_name asc")
    cursor.execute("select proc_name,"
                    + "p.remarks as proc_remarks,"
                    + "parm_id,"
                    + "parm_name,"
                    + "parm_type,"
                    + "parm_mode_in as mode_in,"
                    + "parm_mode_out as mode_out,"
                    + "base_type_str as parm_datatype,"
                    + "width,"
                    + "scale,"
                    + '"default",'
                    + "parm.remarks as param_remarks "
                    + "from " 
                    + "sys.sysprocedure as p " 
                    + "join "
                    + "sys.sysprocparm as parm "
                    + "on p.proc_id = parm.proc_id "
                    + "where p.creator = 101 and proc_defn like 'create procedure%' and p.remarks like '<module>%' " 
                    + "order by proc_name asc, parm.parm_id asc")
    return cursor.fetchall()

def fetch_functions(cursor):
    # cursor.execute("Select proc_name, remarks from sys.sysprocedure where creator = 101 and proc_defn like 'create function%' and remarks like '<module>%' order by proc_name asc")
    cursor.execute("select proc_name,"
                    + "p.remarks as proc_remarks,"
                    + "parm_id,"
                    + "parm_name,"
                    + "parm_type,"
                    + "parm_mode_in as mode_in,"
                    + "parm_mode_out as mode_out,"
                    + "base_type_str as parm_datatype,"
                    + "width,"
                    + "scale,"
                    + '"default",'
                    + "parm.remarks as param_remarks "
                    + "from " 
                    + "sys.sysprocedure as p " 
                    + "join "
                    + "sys.sysprocparm as parm "
                    + "on p.proc_id = parm.proc_id "
                    + "where p.creator = 101 and proc_defn like 'create function%' and p.remarks like '<module>%' " 
                    + "order by proc_name asc, parm.parm_id asc")
    return cursor.fetchall()

def fetch_tables(cursor):
    cursor.execute("""select 
            tab.table_name,
            col.cname,
            col.coltype,
            col.nulls,
            col.length,
            col.syslength,
            col.in_primary_key,
            col.colno,
            col.default_value,
            col.column_kind,
            tab.remarks as table_remarks,
            col.remarks as column_remarks,
            primary_tname as foreign_key_origin,
            column_name_primary as foreign_key_origin_name,
            tm.remarks as foreign_key_origin_remarks,
            rb.referenced_by_table_names,
            rb.referenced_by_column_names,
            rb.referenced_by_remarks
            from sys.systable as tab
            join 
            sys.syscolumns as col
            on col.tname = tab.table_name
            left outer join 
            (select 
            foreign_tname, 
            primary_tname, 
            substring(columns, 0, charindex(' IS ', columns)) as column_name_foreign, 
            substring(columns, charindex(' IS ', columns) + 4, length(columns)) as column_name_primary
            from sys.sysforeignkeys) as fk
            on tab.table_name = fk.foreign_tname and col.cname = fk.column_name_foreign
            left outer join sys.systable as tm
            on foreign_key_origin = tm.table_name 
            left outer join
            ( select t.table_name, c.column_name, list(ft.table_name, '|') as referenced_by_table_names, list(fc.column_name, '|') as referenced_by_column_names, list(ft.remarks, '|') as referenced_by_remarks from
            sys.systable t
            right outer join
            sys.syscolumn c
            on c.table_id = t.table_id
            left outer join
            (select b.primary_table_id, a.foreign_table_id, a.foreign_column_id, a.primary_column_id from sys.SYSFKCOL a 
            join sys.sysForeignkey b
            on a.foreign_table_id = b.foreign_table_id and a.foreign_key_id = b.foreign_key_id) as f
            on t.table_id = f.primary_table_id and c.column_id = f.primary_column_id
            join 
            sys.systable ft 
            on ft.table_id = f.foreign_table_id 
            right outer join 
            sys.syscolumn fc 
            on fc.table_id = f.foreign_table_id and fc.column_id = f.foreign_column_id 
            where t.creator = 101 and ft.remarks like '<module>%'
            group by t.table_name, c.column_name) as rb 

            on rb.table_name = tab.table_name and col.cname = rb.column_name 

            where tab.table_type = 'BASE' and tab.creator = 101 and tab.remarks like '<module>%'
            order by tab.table_name asc, col.colno asc""")
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