#!/usr/bin/env python
"""Main script."""
import argparse
import json


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
    key_list = list(file1.keys())
    key_list.extend(list(filter(
        lambda key: key not in key_list,
        list(file2.keys()),
    )))
    res = '{\n'

    for key in sorted(key_list):
        item_for_file1 = file1.get(key)
        item_for_file2 = file2.get(key)
        if item_for_file1 is None:
            res += '  {0} {1}: {2}\n'.format('+', key, item_for_file2)
            continue
        if item_for_file2 is None:
            res += '  {0} {1}: {2}\n'.format('-', key, item_for_file1)
            continue
        if item_for_file1 == item_for_file2:
            res += '    {0}: {1}\n'.format(key, item_for_file1)
            continue
        if item_for_file1 != item_for_file2:
            res += '  {0} {1}: {2}\n'.format('-', key, item_for_file1)
            res += '  {0} {1}: {2}\n'.format('+', key, item_for_file2)

    res += '}'
    return res


if __name__ == '__main__':
    main()
