from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.plain import formatter_plain


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return formatter_stylish(diff)
    elif formatter == 'plain':
        return formatter_plain(diff)
    else:
        raise ValueError(f"Unknown formatter: {formatter}")
