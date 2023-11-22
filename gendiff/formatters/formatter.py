from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.json import formatter_json


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return formatter_stylish(diff)
    elif formatter == 'plain':
        return formatter_plain(diff)
    elif formatter == 'json':
        return formatter_json(diff)
    else:
        raise ValueError(f"Unknown formatter: {formatter}")
