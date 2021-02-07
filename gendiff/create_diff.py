def create_diff(data1, data2=None):
    """
    Create a diff for a given dictionaries.
    Parameters:
        data1: The first dictionary to compare.
        data2: The second dictionary to compare.
    Returns:
        Diff of the given dictionaries.
    """

    if type(data1) != dict:
        return data1

    if data2 is None:
        data2 = data1

    keys = create_list_keys(data1, data2)

    result = {}

    for key in sorted(keys):
        if key in data1 and key not in data2:
            result[key] = {
                'status': 'deleted',
                'value': create_diff(data1[key])
            }
        elif key in data2 and key not in data1:
            result[key] = {
                'status': 'added',
                'value': create_diff(data2[key])
            }
        else:
            if (type(data1[key]) != dict) or (type(data2[key]) != dict):
                result[key] = {
                    'status': 'replaced',
                    'value': create_diff(data1[key]),
                    'value2': create_diff(data2[key])
                }
            elif data1[key] == data2[key]:
                result[key] = {
                    'status': 'unchanged',
                    'value': create_diff(data1[key])
                }
            else:
                result[key] = {
                    'status': 'changed',
                    'value': create_diff(data1[key], data2[key])
                }

    return result


def create_list_keys(dict1, dict2):
    """
    Create a diff for a given dictionaries.
    Parameters:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.
    Returns:
        Keys from dict1 and dict2
    """
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())

    return keys1 if (dict1 == dict2) else set(keys1 + keys2)
