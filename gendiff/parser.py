import json
import yaml


def get_file_path(file_path):
    if file_path.endswith('.json'):
        file_type = 'json'
    elif file_path.endswith(('.yaml', '.yml')):
        file_type = 'yaml'
    else:
        raise NameError(f'File "{file_path}" not correct format')

    with open(file_path) as file:
        data = parse_file(file, file_type)
    return data


def parse_file(file_content, file_type):
    if file_type == 'json':
        return json.load(file_content)
    elif file_type == 'yaml':
        data = yaml.safe_load(file_content)
        return data or {}
    else:
        raise ValueError(f'File extention "{file_type}" '
                         f'have to be .json or .yaml')
