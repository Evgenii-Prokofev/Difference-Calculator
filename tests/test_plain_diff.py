from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'


def test_plain_json_data():
    file3 = 'tests/fixtures/file3.json'
    file4 = 'tests/fixtures/file4.json'
    with open(PATH + 'result_format_plain.txt', 'r') as expected_file:
        expected_result = expected_file.read()
    result = generate_diff(file3, file4, formatter='plain')
    assert result == expected_result
