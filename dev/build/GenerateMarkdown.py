import os

def generate_procedure_markdown(procedure):
    if not os.path.exists(f'../database/{procedure.module}'):
        os.mkdir(f'../database/{procedure.module}')
    if not os.path.exists(f'../database/{procedure.module}/procedures/'):
        os.mkdir(f'../database/{procedure.module}/procedures/')
    with open(f'../database/{procedure.module}/procedures/{procedure.name}.md', 'w+') as f:
        write_line(f, f'# {procedure.name}')
        write_line(f, procedure.comment)

def generate_table_markdown(table):
    if not os.path.exists(f'../database/{table.module}'):
        os.mkdir(f'../database/{table.module}')
    if not os.path.exists(f'../database/{table.module}/tables/'):
        os.mkdir(f'../database/{table.module}/tables/')
    with open(f'../database/{table.module}/tables/{table.name}.md', 'w+') as f:
        write_line(f, f'# {table.name}')
        write_line(f, table.comment)
        write_line(f,'## Columns')
        write_line(f, '| Nr | Name | Datatype | Null allowed | Length | Decimal digits | In Primary Key | Default Value |')
        write_line(f, '| --- | --- | --- | --- | --- | :---: | --- | --- |')
        for column in table.columns:
            column_string = f'| {column["colno"]} | {column["name"]} | {column["coltype"]} |'
            column_string += ' true |' if column['nulls'] == 'Y' else ' false |'
            column_string += f' {column["length"]} |'
            column_string += ' - |' if not any(x in column['coltype'] for x in ('decimal', 'numeric')) else f'{column["syslength"]} |'
            column_string += ' true |' if column['in_primary_key'] == 'Y' else ' false |'
            column_string += ' null |' if not column["default_value"] else f'{column["default_value"]} |' 
            write_line(f, column_string)

def generate_view_markdown(view):
    if not os.path.exists(f'../database/{view.module}'):
        os.mkdir(f'../database/{view.module}')
    if not os.path.exists(f'../database/{view.module}/views/'):
        os.mkdir(f'../database/{view.module}/views/')
    with open(f'../database/{view.module}/views/{view.name}.md', 'w+') as f:
        write_line(f, f'# {view.name}')
        write_line(f, view.comment)
        write_line(f,'## Columns')
        write_line(f, '| Nr | Name | Datatype | Null possible | Length | Decimal digits |')
        write_line(f, '| --- | --- | --- | --- | --- | :---: |')
        for column in view.columns:
            column_string = f'| {column["colno"]} | {column["name"]} | {column["coltype"]} |'
            column_string += ' true |' if column['nulls'] == 'Y' else ' false |'
            column_string += f' {column["length"]} |'
            column_string += ' - |' if not any(x in column['coltype'] for x in ('decimal', 'numeric')) else f'{column["syslength"]} |'
            write_line(f, column_string)
        
def write_line(file, string):
    file.write(f'{string}\n')