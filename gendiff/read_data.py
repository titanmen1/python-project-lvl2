import os
import json
import yaml


def read_data(path):
    _, extension = os.path.splitext(path)
    extension = extension.lower()

    with open(path, 'r') as data_from_file:
        if extension == '.json':
            return json.load(data_from_file)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(data_from_file)
