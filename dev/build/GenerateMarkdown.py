import os
import xml.etree.ElementTree as ET

def generate_procedure_markdown(procedure):
    if not os.path.exists(f'../database/{procedure.module}'):
        os.mkdir(f'../database/{procedure.module}')
    if not os.path.exists(f'../database/{procedure.module}/Procedures/'):
        os.mkdir(f'../database/{procedure.module}/Procedures/')
    with open(f'../database/{procedure.module}/Procedures/{procedure.name}.md', 'w+') as f:
        write_line(f, f'# {procedure.name}')
        write_line(f, procedure.comment)

        if procedure.deprecated:
            write_line(f, '## Deprecated')
            write_line(f, procedure.deprecated_description)
            if procedure.has_use_instead:
                if procedure.use_instead_module == procedure.module:
                    write_line(f, f'It is advised to use [{procedure.use_instead_name}]({procedure.use_instead_name}.md) instead.')
                else:
                    write_line(f, f'It is advised to use [{procedure.use_instead_name}](../../{procedure.use_instead_module}/Procedures/{procedure.use_instead_name}.md) instead.')
       
        write_line(f, '## Params')
        write_line(f, '| Nr | Name | Type | Mode | Datatype | Length | Decimal Digits | Default Value | Description |')
        write_line(f, '| --- | --- | --- | --- | --- | --- | :---: | --- | --- |')
        for param in procedure.params:
            row_string = f'| {param["id"]} | {param["name"]} | {param["type"]} |'
           
            if param["mode_in"] == 'Y' and param["mode_out"] == 'Y':
                row_string += ' IN & OUT |'
            elif param["mode_in"] == 'Y':
                row_string += ' IN |'
            else:
                row_string += ' OUT |'
            
            row_string += f' {param["datatype"]} | {param["length"]} |'
            row_string += ' - |' if not any(x in param['datatype'] for x in ('decimal', 'numeric')) else f'{param["scale"]} |'
            row_string += ' null |' if not param["default"] else f'{param["default"]} |'
            row_string += f'{param["remarks"]} |' if param['remarks'] else ' |'
            write_line(f, row_string)

def generate_function_markdown(function):
    if not os.path.exists(f'../database/{function.module}'):
        os.mkdir(f'../database/{function.module}')
    if not os.path.exists(f'../database/{function.module}/Functions/'):
        os.mkdir(f'../database/{function.module}/Functions/')
    with open(f'../database/{function.module}/Functions/{function.name}.md', 'w+') as f:
        write_line(f, f'# {function.name}')
        write_line(f, function.comment)
    
        if function.deprecated:
            write_line(f, '## Deprecated')
            write_line(f, function.deprecated_description)
            if function.has_use_instead:
                if function.use_instead_module == function.module:
                    write_line(f, f'It is advised to use [{function.use_instead_name}]({function.use_instead_name}.md) instead.')
                else:
                    write_line(f, f'It is advised to use [{function.use_instead_name}](../../{function.use_instead_module}/Functions/{function.use_instead_name}.md) instead.')

        write_line(f, '## Params')
        write_line(f, '| Nr | Name | Type | Mode | Datatype | Length | Decimal Digits | Default Value | Description |')
        write_line(f, '| --- | --- | --- | --- | --- | --- | :---: | --- | --- |')
        for param in function.params:
            row_string = f'| {param["id"]} | {param["name"]} | {param["type"]} |'
            
            if param["mode_in"] == 'Y' and param["mode_out"] == 'Y':
                row_string += ' IN & OUT |'
            elif param["mode_in"] == 'Y':
                row_string += ' IN |'
            else:
                row_string += ' OUT |'
            
            row_string += f' {param["datatype"]} | {param["length"]} |'
            row_string += ' - |' if not any(x in param['datatype'] for x in ('decimal', 'numeric')) else f'{param["scale"]} |'
            row_string += ' null |' if not param["default"] else f'{param["default"]} |'
            row_string += f'{param["remarks"]} |' if param['remarks'] else ' |'
            write_line(f, row_string)

def generate_table_markdown(table):
    if not os.path.exists(f'../database/{table.module}'):
        os.mkdir(f'../database/{table.module}')
    if not os.path.exists(f'../database/{table.module}/Tables/'):
        os.mkdir(f'../database/{table.module}/Tables/')
    with open(f'../database/{table.module}/Tables/{table.name}.md', 'w+') as f:
        write_line(f, f'# {table.name}')
        write_line(f, table.comment)

        if table.deprecated:
            write_line(f, '## Deprecated')
            write_line(f, table.deprecated_description)
            if table.has_use_instead:
                if table.use_instead_module == table.module:
                    write_line(f, f'It is advised to use [{table.use_instead_name}]({table.use_instead_name}.md) instead.')
                else:
                    write_line(f, f'It is advised to use [{table.use_instead_name}](../../{table.use_instead_module}/Tables/{table.use_instead_name}.md) instead.')
        
        write_line(f,'## Overview')
        write_line(f, 'This is an overview of the column metadata')
        write_line(f, '| Nr | Name | Datatype | Null Allowed | Length | Decimal Digits | In Primary Key | Default Value | Is Foreign Key |')
        write_line(f, '| --- | --- | --- | --- | --- | :---: | --- | --- | --- |')
        for column in table.columns:
            column_string = f'| {column["colno"]} | [{column["name"]}](#{column["name"].lower().replace("_","")}) | {column["coltype"]} |'
            column_string += ' true |' if column['nulls'] == 'Y' else ' false |'
            column_string += f' {column["length"]} |'
            column_string += ' - |' if not any(x in column['coltype'] for x in ('decimal', 'numeric')) else f'{column["syslength"]} |'
            column_string += ' true |' if column['in_primary_key'] == 'Y' else ' false |'
            column_string += ' null |' if not column["default_value"] else f'{column["default_value"]} |'
            column_string += ' true |' if column['foreign_key_origin'] else ' false |'
            write_line(f, column_string)
        write_line(f, '## Columns')
        for column in table.columns:
            write_line(f, f'### {column["name"]}')
            write_line(f, column['column_remarks'])

            if column['referenced_by_table_names'] and column['referenced_by_column_names'] and column['referenced_by_remarks']:
                # print(column['name'] + table.name)
                write_line(f, "#### Referenced by")
                tables_referencing_this = column['referenced_by_table_names'].split('|')
                columns_referencing_this = column['referenced_by_column_names'].split('|')
                referencing_this_remarks = column['referenced_by_remarks'].split('|')

                for foreign_table, foreign_column_name, foreign_remarks in zip(tables_referencing_this, columns_referencing_this, referencing_this_remarks):
                    root = ET.fromstring(f'<xml>{foreign_remarks}</xml>')
                    if root:
                        module = root.find('module').text
                        if module == table.module:
                            write_line(f,f'[{foreign_table}]({foreign_table}.md#{foreign_column_name.lower().replace("_","")}) as {foreign_column_name}  ')
                        else:
                            write_line(f,f'[{foreign_table}](../../{module}/Tables/{foreign_table}.md#{foreign_column_name.lower().replace("_","")})  as {foreign_column_name}  ')

            write_line(f, '| Nr | Datatype | Null allowed | Length | Decimal digits | In Primary Key | Default Value | Foreign Key Origin |')
            write_line(f, '| --- | --- | --- | --- | :---: | --- | --- | :---: |')
            
            row_string = f'| {column["colno"]} | {column["coltype"]} | '
            row_string += ' true |' if column['nulls'] == 'Y' else ' false |'
            row_string += f' {column["length"]} |'
            row_string += ' - |' if not any(x in column['coltype'] for x in ('decimal', 'numeric')) else f'{column["syslength"]} |'
            row_string += ' true |' if column['in_primary_key'] == 'Y' else ' false |'
            row_string += ' null |' if not column["default_value"] else f'{column["default_value"]} |'
            row_string += f' [{column["foreign_key_origin"]}]' if column["foreign_key_origin"] else ' - |'

            # This needs some heavy testing first
            if column["foreign_key_origin"]:
                # print(column["foreign_key_origin_remarks"])
                if column["foreign_key_origin_remarks"]:
                    root = ET.fromstring(f'<xml>{column["foreign_key_origin_remarks"]}</xml>')
                    if root:
                        foreign_module = root.find('module').text
                        if foreign_module == table.module:
                            row_string += f'({column["foreign_key_origin"]}.md#{column["foreign_key_origin_name"].lower().replace("_","")}) |'
                        else:
                            row_string += f'(../../{foreign_module}/Tables/{column["foreign_key_origin"]}.md#{column["foreign_key_origin_name"].lower().replace("_","")}) |'
                    else:
                        row_string += '(../../table_not_added.md) |' 
                        print('Foreign key has wrong remarks syntax!')
                else:
                    row_string += '(../../table_not_added.md) |' 
                    print('Foreign key has no remarks set yet!')
            write_line(f, row_string)

def generate_view_markdown(view):
    if not os.path.exists(f'../database/{view.module}'):
        os.mkdir(f'../database/{view.module}')
    if not os.path.exists(f'../database/{view.module}/Views/'):
        os.mkdir(f'../database/{view.module}/Views/')
    with open(f'../database/{view.module}/Views/{view.name}.md', 'w+') as f:
        write_line(f, f'# {view.name}')
        write_line(f, view.comment)

        if view.deprecated:
            write_line(f, '## Deprecated')
            write_line(f, view.deprecated_description)
            if view.has_use_instead:
                if view.use_instead_module == view.module:
                    write_line(f, f'It is advised to use [{view.use_instead_name}]({view.use_instead_name}.md) instead.')
                else:
                    write_line(f, f'It is advised to use [{view.use_instead_name}](../../{view.use_instead_module}/Views/{view.use_instead_name}.md) instead.')

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
