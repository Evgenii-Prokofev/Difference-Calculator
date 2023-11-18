from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
FILE3 = 'tests/fixtures/file3.yaml'
FILE4 = 'tests/fixtures/file4.yaml'
FILE5 = 'tests/fixtures/file5.json'
FILE6 = 'tests/fixtures/file6.json'


def test_nested_json_data():
    file3 = 'tests/fixtures/file3.json'
    file4 = 'tests/fixtures/file4.json'
    with open(PATH + 'result_format_stylish.txt', 'r') as expected_file:
        expected_result = expected_file.read()
    result = generate_diff(file3, file4)
    assert result == expected_result


@pytest.mark.parametrize("file1, file2, expected", [
    (f'{FILE5}', f'{FILE6}', 'result_yaml_stylish.txt'),
    (f'{FILE3}', f'{FILE4}', 'result_yaml_stylish.txt'),
    (f'{FILE5}', f'{FILE4}', 'result_yaml_stylish.txt')])
def test_nested_with_my_data(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result