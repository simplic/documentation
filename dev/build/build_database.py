import os
import urllib
import pyodbc
import xml.etree.ElementTree as ET
import argparse
from DatabaseStatements import fetch_procedures, fetch_tables, fetch_views, fetch_functions
from GenerateMarkdown import generate_procedure_markdown, generate_view_markdown, generate_table_markdown, generate_function_markdown

class SQLObject:
    def __init__(self, name, remarks):
        self.name = name
        print(f'<xml>{remarks}</xml>')
        root = ET.fromstring(f'<xml>{remarks}</xml>')
        self.module = root.find('module').text
        self.comment = root.find('description').text
        
        if root.find('deprecated'):
            self.deprecated = True
            self.use_instead_module = root.find('deprecated').find('module').text
            self.use_instead_name = root.find('deprecated').find('name').text
        else:
            self.deprecated = False

class Table(SQLObject):
    def __init__(self, name, remarks, raw_column_metadata):
        super().__init__(name, remarks)
        
        self.columns = []

        next_column_name = ''
        next_foreign_key_origin = ''
        next_foreign_key_origin_name = ''
        for row in raw_column_metadata:
            column = {'name': row[1], 'coltype': row[2], 'nulls': row[3], 'length': row[4], 'syslength': row[5],
                     'in_primary_key': row[6], 'colno': row[7], 'default_value': row[8], 'column_kind': row[9],
                     'column_remarks': row[11], 'foreign_key_origin': row[12],  'foreign_key_origin_name': row[13],
                      'foreign_key_origin_remarks': row[14], 'referenced_by_table_names': row[15], 
                      'referenced_by_column_names': row[16], 'referenced_by_remarks': row[17]}
            # Multiple columns as a foreign key handeling TODO: untested!
            if column['name'] == next_column_name:
                column['foreign_key_origin'] = next_foreign_key_origin
                column['foreign_key_origin_name'] = next_foreign_key_origin_name
                next_column_name = ''
                next_foreign_key_origin = ''
                next_foreign_key_origin_name = ''
            if column['foreign_key_origin_name']:
                if ',' in column['foreign_key_origin_name']:
                    column['foreign_key_origin_name'] = column['foreign_key_origin_name'].split(',')[0]
                    next_foreign_key_origin = column['foreign_key_origin']
                    next_column_name = column['foreign_key_origin_name'].split(',', 1)[1].split(' IS ')[0]
                    next_foreign_key_origin_name = column['foreign_key_origin_name'].split(',', 1)[1].split(' IS ')[1]

            self.columns.append(column)

class View(SQLObject):
    def __init__(self, name, remarks, raw_column_metadata):
        super().__init__(name, remarks)

        self.columns = []
        for row in raw_column_metadata:
            column = {'name': row[0], 'coltype': row[1], 'nulls': row[2], 'length': row[3], 'syslength': row[4],
                     'in_primary_key': row[5], 'colno': row[6], 'default_value': row[7], 'column_kind': row[8]}
            self.columns.append(column)

# Filter what tables / views the procedure alters / uses later maybe
class Procedure(SQLObject):
    def __init__(self, name, remarks, raw_params):
        super().__init__(name, remarks)

        self.params = []
        for row in raw_params:
            param = {'id': row[0], 'name': row[1], 'type': row[2], 'mode_in': row[3], 'mode_out': row[4],'datatype': row[5],
                     'length': row[6], 'scale': row[7], 'default': row[8], 'remarks': row[9]}
            self.params.append(param)
    
    def __repr__(self):
        return str({'name': self.name, 'module': self.module, 'comment': self.comment})

class Function(SQLObject):
    def __init__(self, name, remarks, raw_params):
        super().__init__(name, remarks)

        self.params = []
        for row in raw_params:
            param = {'id': row[0], 'name': row[1], 'type': row[2], 'mode_in': row[3], 'mode_out': row[4],'datatype': row[5],
                     'length': row[6], 'scale': row[7], 'default': row[8], 'remarks': row[9]}
            self.params.append(param)
    
    def __repr__(self):
        return str({'name': self.name, 'module': self.module, 'comment': self.comment})

def generate_procedures(cur):
    result = fetch_procedures(cur)
    if result:
        procedure_name = result[0][0]
        remarks = result[0][1]
        params = [result[0][2:]]
        for i, row in enumerate(result):
            if row[0] == procedure_name:
                params.append(row[2:])
            else:
                procedure = Procedure(procedure_name, remarks, params)
                generate_procedure_markdown(procedure)
                procedure_name = row[0]
                remarks = row[1]
                params = [row[2:]]
            # print(f'Row {i+1} {row}')
        # Generate last procedure
        procedure = Procedure(procedure_name, remarks, params)
        generate_procedure_markdown(procedure)

def generate_functions(cur):
    result = fetch_functions(cur)
    if result:
        function_name = result[0][0]
        remarks = result[0][1]
        params = [result[0][2:]]
        for i, row in enumerate(result):
            if row[0] == function_name:
                params.append(row[2:])
            else:
                function = Function(function_name, remarks, params)
                generate_function_markdown(function)
                function_name = row[0]
                remarks = row[1]
                params = [row[2:]]
            # print(f'Row {i+1} {row}')
        # Generate last procedure
        function = Function(function_name, remarks, params)
        generate_function_markdown(function)

def generate_views(cur):
    result = fetch_views(cur)
    if result:
        view_name = result[0][0]
        remarks = result[0][-1]
        columns = [result[0][1:-1]]

        for i, row in enumerate(result[1:]):
            if row[0] == view_name:
                columns.append(row[1:-1])
            else:
                view = View(view_name, remarks, columns)
                generate_view_markdown(view)
                view_name = row[0]
                remarks = row[-1]
                columns = [row[1:-1]]
           #  print(f'Row {i+1} {row}')
        # Generate the last view
        view = View(view_name, remarks, columns)
        generate_view_markdown(view)

def generate_tables(cur):
    result = fetch_tables(cur)
    if result:
        table_name = result[0][0]
        remarks = result[0][10]
        columns = [result[0]]

        for i, row in enumerate(result[1:]):
            if row[0] == table_name:
                columns.append(row)
            else:
                table = Table(table_name, remarks, columns)
                generate_table_markdown(table)
                table_name = row[0]
                remarks = row[10]
                columns = [row]
           #  print(f'Row {i+1} {row}')
        # Generate the last view
        table = Table(table_name, remarks, columns)
        generate_table_markdown(table)
    else:
        print("Resultset empty")

def generate_toc_module():
    modules = [f'../database/{d}' for d in os.listdir('../database/') if os.path.isdir(f'../database/{d}') and d != 'database_design']
    database_toc = ''
    for module in modules:
        module_toc = ''
        dirs = [f'{module}/{d}' for d in os.listdir(module) if os.path.isdir(f'{module}/{d}')]
        for _dir in dirs:
            toc = ''
            for f in os.listdir(_dir):
                if f != 'toc.yml':
                    toc += (f'- name: {f.split(".md")[0]}\n'
                        + f'  href: {f}\n')
            module_toc += (f'- name: {_dir.split(f"{module}/")[1]}\n'
                        + f'  href: {_dir.split(f"{module}/")[1]}/toc.yml\n')
            with open(f'{_dir}/toc.yml', 'w+') as _f:
                _f.write(toc)
        database_toc += (f'- name: {module.split("../database/")[1]}\n'
                    + f'  href: {module.split("../database/")[1]}/toc.yml\n')
        with open(f'{module}/toc.yml', 'w+') as _f:
            _f.write(module_toc)
    with open('../database/toc.yml', 'a+') as _f:
        _f.write(database_toc)


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--conn-strings', help='Pass a variable amount of connection strings, seperated by whitespaces.', nargs='+')
args = vars(parser.parse_args())

if not args['conn_strings']:
    print('Enter atleast one connection string. Get a list of the arguments by adding --help to the script call. e.g. python build_database.py --help')
    exit()

for conn_string in args['conn_strings']:
    conn = pyodbc.connect(conn_string)
    cur = conn.cursor()

    generate_procedures(cur)
    generate_functions(cur)
    generate_views(cur)
    generate_tables(cur)

    cur.close()
    conn.close()
generate_toc_module()
