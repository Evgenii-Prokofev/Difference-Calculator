import json


def get_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def generate_diff(file1, file2):
    dict1 = get_data(file1)
    dict2 = get_data(file2)
    data = {}

    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    kept = dict1.keys() & dict2.keys()
    for key in removed:
        data.update({key: {'prefix': '-'}})
        data[key].update({'name': key})
        data[key].update({'data':  dict1[key]})
    for key in added:
        data.update({key: {'prefix': '+'}})
        data[key].update({'name': key})
        data[key].update({'data':  dict2[key]})
    for key in kept:
        if dict1[key] == dict2[key]:
            data.update({key:  {'prefix':  ' '}})
            data[key].update({'name': key})
            data[key].update({'data': dict1[key]})
        else:
            data.update({f'{key}1': {'prefix': '-'}})
            data[f'{key}1'].update({'name': key})
            data[f'{key}1'].update({'data':  dict1[key]})
            data.update({f'{key}2': {'prefix': '+'}})
            data[f'{key}2'].update({'name': key})
            data[f'{key}2'].update({'data':  dict2[key]})

    result = dict(sorted(data.items()))
    output = ''
    for value in result.values():
        output = f'{output} {value["prefix"]} {value["name"]}: {value["data"]}\n'
    return f'{{\n{output}}}'