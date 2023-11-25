from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
FILE3 = 'tests/fixtures/file3.json'
FILE4 = 'tests/fixtures/file4.json'


@pytest.mark.parametrize("file1, file2, expected", [
    (f'{FILE3}', f'{FILE4}', 'result_format_json.txt'),])
def test_format_json_data(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2, formatter='json') == expected_result
