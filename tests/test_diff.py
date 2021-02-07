import pytest
from gendiff.gendiff import generate_diff


def test_gendiff_json():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    output = './tests/fixtures/output.json'
    assert generate_diff(file1, file2, 'json') == open(output, 'r').read()
