import pytest
from gendiff.gendiff import generate_diff


def test_gendiff_json():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    assert generate_diff(file1, file2) ==

    assert generate_diff(file2, file1) ==
