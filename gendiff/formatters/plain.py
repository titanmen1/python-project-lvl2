def to_string(value):
    '''
     Makу representation for key values,
     that were added, deleted or replaced
    Parameters:
        diff: key value
    Return:
        key value formated in string
    '''
    if type(value) == dict or type(value) == list:
        return '[complex value]'
    if type(value) == bool:
        return str(value).lower()
    if value is None:
        return 'null'
    if type(value) == str:
        return "'{}'".format(value)
    return value


def render_plain(diff, path=''):
    """
    Formatting diff in plain format.
    Parameters:
        diff: Dictionary with the diff result rows.
        path: path in dictionary to diff
    Returns:
        String of diff rows, formatted as a plain.
    """
    keys = sorted(diff.keys())
    result = []

    for key in keys:
        path_to_value = path + key
        if diff[key]['status'] == 'unchanged':
            continue
        elif diff[key]['status'] == 'changed':
            string = render_plain(diff[key]['value'], path_to_value + '.')
        else:
            # string = _make_string_from_template(path_to_value, diff, key)
            status = diff[key]['status']
            if status == 'added':
                string = "Property {0} was added with value: {1}".format(path_to_value, to_string(diff[key]['value']))
            if status == 'replaced':
                string = "Property {0} was removed".format(path_to_value)
            if status == 'replaced':
                string = "Property {0} was updated. From {1} to {2}".format(path_to_value,
                                                                            to_string(diff[key]['value']),
                                                                            to_string(diff[key]['value2']))

        result.append(string)

    return '\n'.join(result)
