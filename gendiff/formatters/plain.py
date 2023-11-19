def value_to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def item_to_str(item, path=''):
    actual_key = item.get('name')
    actual_path = f"{path}.{actual_key}" if path else actual_key
    action = item.get('action')
    new_value = value_to_str(item.get('new_value'))
    old_value = value_to_str(item.get('old_value'))

    if action == 'added':
        return f"Property '{actual_path}' was added with value: {new_value}"
    if action == 'deleted':
        return f"Property '{actual_path}' was removed"
    if action == 'modified':
        return (
            f"Property '{actual_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
    if action == 'nested':
        children = item.get('children')
        return make_plain(children, actual_path)
    return None


def make_plain(diff, path=''):
    result = []
    for item in diff:
        formatted_item = item_to_str(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def formatter_plain(data):
    return make_plain(data)
