"""Func for parse args from cli."""
import argparse


def parse():
    """Func for parse args from cli.

    Returns:
        Args from cli
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish',
    )
    return parser.parse_args()
