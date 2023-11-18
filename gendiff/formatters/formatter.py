from gendiff.formatters.stylish import formatter_stylish


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return formatter_stylish(diff)
    else:
        raise ValueError(f"Unknown formatter: {formatter}")
