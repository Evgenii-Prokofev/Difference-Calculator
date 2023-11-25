def generate_added_descriptor(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def generate_deleted_descriptor(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def generate_unchanged_descriptor(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def generate_modified_descriptor(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def generate_nested_descriptor(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': constructor_diff(value1, value2)
    }


def constructor_diff(data1, data2):
    all_keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()

    diff = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in added:
            diff.append(generate_added_descriptor(key, value2))
        elif key in deleted:
            diff.append(generate_deleted_descriptor(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(generate_nested_descriptor(key, value1, value2))
        elif value1 != value2:
            diff.append(generate_modified_descriptor(key, value1, value2))
        else:
            diff.append(generate_unchanged_descriptor(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff
