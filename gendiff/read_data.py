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

    with open(path, 'r') as data_from_file:
        if extension == '.json':
            return json.load(data_from_file)
        elif extension in {'.yml', '.yaml'}:
            return yaml.safe_load(data_from_file)
