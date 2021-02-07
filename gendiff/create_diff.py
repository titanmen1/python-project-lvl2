"""File with func for create diff."""
from gendiff.consts import STATUS, VALUE


def create_diff(data1, data2=None):
    """Create a diff for a given dictionaries.

    Args:
        data1: The first dictionary to compare.
        data2: The second dictionary to compare.

    Returns:
        Diff of the given dictionaries.
    """
    if not isinstance(data1, data1):
        return data1

    if data2 is None:
        data2 = data1

    keys = create_list_keys(data1, data2)

    result_diff = {}

    for key in sorted(keys):
        if key in data1 and key not in data2:
            result_diff[key] = {
                STATUS: 'deleted',
                VALUE: create_diff(data1[key]),
            }
        elif key in data2 and key not in data1:
            result_diff[key] = {
                STATUS: 'added',
                VALUE: create_diff(data2[key]),
            }
        else:
            if not isinstance(data1[key], dict) or not isinstance(data2[key], dict):  # noqa: E501
                result_diff[key] = {
                    STATUS: 'replaced',
                    VALUE: create_diff(data1[key]),
                    'value2': create_diff(data2[key]),
                }
            elif data1[key] == data2[key]:
                result_diff[key] = {
                    STATUS: 'unchanged',
                    VALUE: create_diff(data1[key]),
                }
            else:
                result_diff[key] = {
                    STATUS: 'changed',
                    VALUE: create_diff(data1[key], data2[key]),
                }

    return result_diff


def create_list_keys(dict1, dict2):
    """Create list keys from dict1 and dict2.

    Args:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.

    Returns:
        Keys from dict1 and dict2.
    """
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())

    return keys1 if (dict1 == dict2) else set(keys1 + keys2)
