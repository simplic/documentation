# -----------------------------------------------------------------------
# Script for creating the public python api documentation in mark-down,
# baed on the file: Simplic.IronPythonAPI.xml
# -----------------------------------------------------------------------

# imports
import xml.etree.ElementTree as ET
import os
import shutil


class ModDoc(object):

    def __init__(self):
        self.type_name = ''
        self.summary = ''
        self.example = ''
        self.__methods = list()
        self.__properties = list()

    def add_method(self, method):
        self.__methods.extend([method])

    def get_methods(self):
        return self.__methods

    def get_properties(self):
        return self.__properties


class ModDocMethod(object):

    def __init__(self):
        self.method_name = ''
        self.summary = ''
        self.returns = ''
        self.__parameter = list()

    def add_parameter(self, method):
        self.__parameter.extend([method])

    def get_parameters(self):
        return self.__parameter


class ModDocMehodParameter(object):
    def __ini__(self):
        self.param_name = ''
        self.param_summary = ''


class ModDocProperty(object):
    def __ini__(self):
        self.name = ''
        self.summary = ''
        self.type = ''
        self.example = ''


def get_summary(node):
    for s_node in node.iter('summary'):
        return str(s_node.text).strip()
    return ""


def get_example(node):
    for s_node in node.iter('example'):
        return str(s_node.text).strip()
    return ""


def get_returns(node):
    for s_node in node.iter('returns'):
        return str(s_node.text).strip()
    return ""


def get_module(docs, type_name):
    if type_name in docs:
        return docs[type_name]
    else:
        docs[type_name] = ModDoc()
        return docs[type_name]


def generate_documentation_from_xml(xml_file_path, dest_dir):
    modDocs = dict()

    # open xml file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Parse helpfile in class structure
    for _member in root.iter('members'):
        # Iterate over member
        for member in _member.iter('member'):

            name = member.get('name')

            # Type
            if name.startswith('T:'):
                name = name.replace('T:', '')
                type_name = name.split('.')[-1]

                doc = get_module(modDocs, type_name)
                doc.type_name = type_name
                doc.summary = get_summary(member)
                doc.example = get_example(member)

                print('Type: ' + type_name)

            if name.startswith('P:'):
                name = name.replace('P:', '')
                type_name = name.split('.')[-2]
                property_name = name.split('.')[-1]

                property_doc = ModDocProperty()
                property_doc.type = type_name
                property_doc.name = property_name
                property_doc.summary = get_summary(member)
                property_doc.example = get_example(member)

                doc = get_module(modDocs, type_name)
                doc.get_properties().append(property_doc)

                print('Property: ' + property_name + ' - ' + type_name)

            # Methods
            if name.startswith('M:'):
                name = name.replace('M:', '')

                # Before bracket
                pre_bracket = name.split('(')[0]
                type_name = pre_bracket.split('.')[-2]

                doc = get_module(modDocs, type_name)
                method = ModDocMethod()
                doc.add_method(method)

                method.method_name = pre_bracket.split('.')[-1]
                method.summary = get_summary(member)
                method.returns = get_returns(member)
                print(' Method: ' + method.method_name)

                for param in member.iter('param'):
                    paramDoc = ModDocMehodParameter()

                    paramDoc.param_name = param.get('name')
                    paramDoc.param_summary = str(param.text).strip()

                    method.add_parameter(paramDoc)

                    print('  Parameter: ' + paramDoc.param_name)

                if method.returns:
                    print('  Returns: ' + method.returns)

    # Remove old api-doc directory and create new one
    # base_path = os.path.dirname(os.path.realpath(__file__)) + '\\..\\doc\\py\\'
    base_path = os.path.normpath(dest_dir)

    print('Output dir: ' + base_path)

    try:
        shutil.rmtree(base_path)
    except OSError:
        pass  # currently not existing

    os.makedirs(base_path)

    def write_line(file, text):
        file.write(text + '\n')

    # Go through class structure and generate api documentation
    for key, value in modDocs.items():

        with open(base_path + "\\" + key + '.md', "w") as file:

            print('Type: ' + value.type_name)
            print(value.summary)
            print('')

            write_line(file, '---')
            write_line(file, f'uid: PythonAPI.{value.type_name}')
            write_line(file, '---')

            write_line(file, value.type_name)
            write_line(file, '===')
            write_line(file, '')
            write_line(file, value.summary)
            write_line(file, '')
            write_line(file, '')

            write_line(file, '## Import and usage of the module')
            write_line(file, '### Calling any static methods')
            write_line(file, 'Using simple `import simplic` statement')
            write_line(file, '```')
            write_line(file, 'import simplic')
            write_line(file, '')
            write_line(file, '# usage')
            write_line(file, 'simplic.' + value.type_name + ".METHOD(...)")
            write_line(file, '```')
            write_line(file, 'Using simple `from simplic import ...` statement')
            write_line(file, '```')
            write_line(file, 'from simplic import ' + value.type_name)
            write_line(file, '')
            write_line(file, '# usage')
            write_line(file, value.type_name + ".METHOD(...)")
            write_line(file, '```')
            write_line(file, '')

            if value.example != '':
                write_line(file, '## Example')
                write_line(file, value.example)
                write_line(file, '')

            write_line(file, '')
            write_line(file, '## Properties')

            for property in value.get_properties():
                print(' Property: ' + property.name)

                write_line(file, '')
                write_line(file, '### ' + property.name)
                write_line(file, '')
                #write_line(file, '__Type__: ' + property.type)
                write_line(file, property.summary)

            write_line(file, '')
            write_line(file, '## Methods')

            for method in value.get_methods():
                print(' Method: ' + method.method_name)

                write_line(file, '')
                write_line(file, '### ' + method.method_name)
                write_line(file, method.summary)
                write_line(file, '')

                write_line(file, '| Name | Summary |    |')
                write_line(file, '| --- | --- | ---- |')

                for param in method.get_parameters():
                    print('   ' + param.param_name +
                          ' -> ' + param.param_summary)
                    write_line(file, ' | ' + param.param_name +
                               ' | ' + param.param_summary + ' | |')

                if method.returns is not None and method.returns.strip() != '':
                    write_line(file, '')
                    write_line(file, '__Returns:__')
                    write_line(file, method.returns)
