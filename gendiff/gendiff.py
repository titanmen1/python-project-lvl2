#!/usr/bin/env python
"""Main script."""
import argparse
import json
from gendiff.read_data import read_data


def main():
    """Start main script."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        )
    args = parser.parse_args()
    file1 = json.load(args.__dict__['first_file'])
    file2 = json.load(args.__dict__['second_file'])
    diff = generate_diff(file1, file2)
    print(diff)
    return diff


def generate_diff(file1, file2):
    """Generate diff.

    Args:
        file1: dict file 1
        file2: dict file 2
    Returns:
        diff as str
    """
    data1 = read_data(file1)
    data2 = read_data(file2)
    diff = compare(data_collection1, data_collection2)

    return format_diff(diff, format_name)


if __name__ == '__main__':
    main()
