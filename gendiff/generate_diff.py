from gendiff.parser import get_file_path
from gendiff.formatters.formatter import format_diff
from gendiff.constructor_diff import constructor_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = get_file_path(file_path1)
    data2 = get_file_path(file_path2)
    diff = constructor_diff(data1, data2)
    return format_diff(diff, formatter)
