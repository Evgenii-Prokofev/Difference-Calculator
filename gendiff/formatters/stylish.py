REPLACER = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def stringify(value, spaces_count=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = REPLACER * (spaces_count + 4)
        result = []
        for key, inner_value in value.items():
            formatted_value = stringify(inner_value, spaces_count + 4)
            result.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(result)
        end_indent = REPLACER * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish(diff, spaces_count=2):  # noqa: C901
    indent = REPLACER * spaces_count
    result = []
    for item in diff:
        key_name = item['name']
        old_value = stringify(item.get("old_value"), spaces_count)
        new_value = stringify(item.get("new_value"), spaces_count)
        action = item["action"]
        if action == "unchanged":
            current_value = stringify(item.get("value"), spaces_count)
            result.append(f"{indent}{NONE}{key_name}: {current_value}")
        elif action == "modified":
            result.append(f"{indent}{DELETE}{key_name}: {old_value}")
            result.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == "deleted":
            result.append(f"{indent}{DELETE}{key_name}: {old_value}")
        elif action == "added":
            result.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == 'nested':
            children = make_stylish(
                item.get("children"), spaces_count + 4
            )
            result.append(f"{indent}{NONE}{key_name}: {children}")
    formatted_result = '\n'.join(result)
    end_indent = REPLACER * (spaces_count - 2)

    return f"{{\n{formatted_result}\n{end_indent}}}"


def format_stylish(diff):
    return make_stylish(diff)
