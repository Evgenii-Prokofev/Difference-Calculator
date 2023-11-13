import json
import yaml


def get_data(file):
    if file.endswith('.json'):
        file_type = 'json'
    elif file.endswith(('.yaml', '.yml')):
        file_type = 'yaml'
    else:
        raise NameError(f'File "{file}" not correct format')

    with open(file) as the_file:
        data = parsing_file(the_file, file_type)
    return data


def parsing_file(file_content, file_type):
    if file_type == 'json':
        return json.load(file_content)
    elif file_type == 'yaml':
        data = yaml.safe_load(file_content)
        return data or {}
    else:
        raise NameError(f'File extention "{file_type}" '
                        f'have to be .json or .yaml')
