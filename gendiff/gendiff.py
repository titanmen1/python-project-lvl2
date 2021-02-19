#!/usr/bin/env python
"""Main script."""
from gendiff.diff import build_diff
from gendiff.formatters.format import format_diff
from gendiff.read_data import read_data


def generate_diff(file1, file2, format_name='stylish'):
    """Generate diff.

    Args:
        file1: dict file 1.
        file2: dict file 2.
        format_name: format name.

    Returns:
        diff as str
    """
    data1 = read_data(file1)
    data2 = read_data(file2)
    diff = build_diff(data1, data2)

    return format_diff(diff, format_name)
