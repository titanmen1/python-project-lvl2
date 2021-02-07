#!/usr/bin/env python
"""Main script."""
import argparse

from gendiff.create_diff import create_diff
from gendiff.formatters.format import format_diff
from gendiff.read_data import read_data


def main():
    """Start main script."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        dest='format',
        action='store',
        help='set format of output',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


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
    diff = create_diff(data1, data2)

    return format_diff(diff, format_name)


if __name__ == '__main__':
    main()
