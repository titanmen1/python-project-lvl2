"""Func for formatting diff in plain format."""
from gendiff.consts import STATUS, VALUE

TEMP_ADD = 'Property {0} was added with value: {1}'
TEMP_REM = 'Property {0} was removed'
TEMP_UPD = 'Property {0} was updated. From {1} to {2}'


def to_string(value_to_str):
    """Func for convert value to string.

    Args:
        value_to_str: value.

    Returns:
        Value convert in string.
    """
    if isinstance(value_to_str, (dict, list)):
        return '[complex value]'
    if isinstance(value_to_str, bool):
        return str(value_to_str).lower()
    if value_to_str is None:
        return 'null'
    if isinstance(value_to_str, str):
        return "'{0}'".format(value_to_str)
    return value_to_str


def render_plain(diff, path=''):
    """Render diff in plain format.

    Args:
        diff: Dictionary with the diff result rows.
        path: path in dictionary to diff.

    Returns:
        String of diff rows, formatted as a plain.
    """
    keys = sorted(diff.keys())
    result_render = []

    for key in keys:
        path_to_value = path + key
        if diff[key][STATUS] == 'unchanged':
            continue
        elif diff[key][STATUS] == 'changed':
            string = render_plain(
                diff[key][VALUE],
                '{0}.'.format(path_to_value),
            )
        else:
            status = diff[key][STATUS]
            if status == 'added':
                string = TEMP_ADD.format(
                    path_to_value,
                    to_string(diff[key][VALUE]),
                )
            if status == 'replaced':
                string = TEMP_REM.format(path_to_value)
            if status == 'replaced':
                string = TEMP_UPD.format(
                    path_to_value,
                    to_string(diff[key][VALUE]),
                    to_string(diff[key]['value2']),
                )

        result_render.append(string)

    return '\n'.join(result_render)
