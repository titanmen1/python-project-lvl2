import pytest
from gendiff.gendiff import generate_diff


def test_gendiff():
    file1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    file2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    assert generate_diff(file1, file2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert generate_diff(file2, file1) == """{
  + follow: False
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: True
}"""
