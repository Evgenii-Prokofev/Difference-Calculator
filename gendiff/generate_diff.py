from gendiff.parsing import get_data
from gendiff.formatters.formatter import format_diff
from gendiff.constructor_diff import constructor_diff


def generate_diff(file1, file2, formatter='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = constructor_diff(data1, data2)
    return format_diff(diff, formatter)
