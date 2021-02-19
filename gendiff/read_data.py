"""Func for reading files."""
import json
import os

import yaml


def read_data(path):
    """Func for reading files.

    Args:
        path: path to file.

    Returns:
        data from file json or yaml.
    """
    _, extension = os.path.splitext(path)
    extension = extension.lower()
    file = open(path)
    return parse(file, extension)


def parse(data, format_type):
    """Func for parse files.

    Args:
        data: data to parse.
        format_type: type format

    Returns:
        data formatting to json or yaml.
    """
    if format_type == '.json':
        return json.load(data)
    elif format_type in {'.yml', '.yaml'}:
        return yaml.safe_load(data)
