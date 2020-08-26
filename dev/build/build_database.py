import os
import urllib
import pyodbc
import xml.etree.ElementTree as ET
import argparse
from DatabaseStatements import fetch_procedures, fetch_tables, fetch_views
from GenerateMarkdown import generate_procedure_markdown, generate_view_markdown, generate_table_markdown

class Table:
    def __init__(self, name, remarks, raw_column_metadata):
        self.name = name
        root = ET.fromstring(f'<xml>{remarks}</xml>')
        self.module = root.find('module').text
        self.comment = root.find('description').text
        self.columns = []
        for row in raw_column_metadata:
            column = {'name': row[0], 'coltype': row[1], 'nulls': row[2], 'length': row[3], 'syslength': row[4],
                     'in_primary_key': row[5], 'colno': row[6], 'default_value': row[7], 'column_kind': row[8]}
            self.columns.append(column)

class View:
    def __init__(self, name, remarks, raw_column_metadata):
        self.name = name
        root = ET.fromstring(f'<xml>{remarks}</xml>')
        self.module = root.find('module').text
        self.comment = root.find('description').text
        self.columns = []
        for row in raw_column_metadata:
            column = {'name': row[0], 'coltype': row[1], 'nulls': row[2], 'length': row[3], 'syslength': row[4],
                     'in_primary_key': row[5], 'colno': row[6], 'default_value': row[7], 'column_kind': row[8]}
            self.columns.append(column)

# Filter what tables / views the procedure alters / uses later maybe
class Procedure:
    def __init__(self, name, remarks):
        self.name = name
        root = ET.fromstring(f'<xml>{remarks}</xml>')
        self.module = root.find('module').text
        self.comment = root.find('description').text
    
    def __repr__(self):
        return str({'name': self.name, 'module': self.module, 'comment': self.comment})

def generate_procedures(cur):
    result = fetch_procedures(cur)
    if result:
        for i, row in enumerate(result):
            procedure_name = row[0]
            remarks = row[1]
            procedure = Procedure(procedure_name, remarks)
            generate_procedure_markdown(procedure)
            print(f'Row {i+1} {row}')

def generate_views(cur):
    result = fetch_views(cur)
    if result:
        view_name = result[0][0]
        remarks = result[0][-1]
        columns = [result[0][1:-1]]

        for i, row in enumerate(result[1:]):
            if row[0] == view_name:
                columns.append(row[1:-1])
            elif view_name:
                view = View(view_name, remarks, columns)
                generate_view_markdown(view)
                view_name = row[0]
                remarks = row[-1]
                columns = [row[1:-1]]
            print(f'Row {i+1} {row}')
        # Generate the last view
        view = View(view_name, remarks, columns)
        generate_view_markdown(view)

def generate_tables(cur):
    result = fetch_tables(cur)
    if result:
        table_name = result[0][0]
        remarks = result[0][-1]
        columns = [result[0][1:-1]]

        for i, row in enumerate(result[1:]):
            if row[0] == table_name:
                columns.append(row[1:-1])
            elif table_name:
                table = Table(table_name, remarks, columns)
                generate_table_markdown(table)
                table_name = row[0]
                remarks = row[-1]
                columns = [row[1:-1]]
            print(f'Row {i+1} {row}')
        # Generate the last view
        table = Table(table_name, remarks, columns)
        generate_table_markdown(table)

def generate_toc_module():
    modules = [f'../database/{d}' for d in os.listdir('../database/') if os.path.isdir(f'../database/{d}')]
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
    with open('../database/toc.yml', 'w+') as _f:
        _f.write(database_toc)


parser = argparse.ArgumentParser()
parser.add_argument('--conn-string', help='The full database connection string - Including Driver, Server, Host, Port, Database, UID and PWD.')
args = vars(parser.parse_args())

connection_string = args['conn_string']

if not connection_string:
    print('Enter all Arguments. Get a list of the arguments by adding --help to the script call. e.g. python build_database.py --help')
    exit()  

conn = pyodbc.connect(connection_string)
cur = conn.cursor()

generate_procedures(cur)
generate_views(cur)
generate_tables(cur)
generate_toc_module()


cur.close()
conn.close()



