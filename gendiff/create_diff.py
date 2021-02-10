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
    if not isinstance(data1, dict):
        return data1

    if data2 is None:
        data2 = data1

    keys = create_list_keys(data1, data2)

    result_diff = []
    for key in sorted(keys):
        if key not in data1:
            result_diff.append({
                'type': "added",
                'key': key,
                'value': data2[key]
            })
            continue

        if key not in data2:
            result_diff.append({
                'type': "removed",
                'key': key,
                'value': data1[key]
            })
            continue

        if isinstance(
                data1[key],
                dict
        ) and isinstance(data2[key], dict):
            result_diff.append({
                'type': "nested",
                'key': key,
                'children': create_diff(data1[key], data2[key])
            })
            continue

        if data1[key] != data2[key]:
            result_diff.append({
                'type': "updated",
                'key': key,
                'old_value': data1[key],
                'new_value': data2[key]
            })
            continue

        result_diff.append({
            'type': "unchanged",
            'key': key,
            'value': data1[key]
        })

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


def build_diff(data1, data2):
    return {
        'type': "origin",
        'children': create_diff(data1, data2)
    }
