import pytest
import json
from gendiff import generate_diff

test_cases = ['yml', 'json']


@pytest.mark.parametrize('test_format', test_cases)
def test_gendiff_json(test_format):
    file1 = './tests/fixtures/file1.{0}'.format(test_format)
    file2 = './tests/fixtures/file2.{0}'.format(test_format)
    output = './tests/fixtures/output.json' if test_format == 'json' else './tests/fixtures/output_for_yml.json'
    assert json.loads(generate_diff(file1, file2, 'json')) == json.load(open(output, 'r'))
    output = './tests/fixtures/test_plain_json' if test_format == 'json' else './tests/fixtures/test_plain'
    assert generate_diff(file1, file2, 'plain') == open(output, 'r').read()
    output = './tests/fixtures/test_stylish_json' if test_format == 'json' else './tests/fixtures/test_stylish'
    assert generate_diff(file1, file2) == open(output, 'r').read()
