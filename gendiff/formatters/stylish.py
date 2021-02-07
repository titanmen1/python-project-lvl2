"""Func for formatting diff in stylish format."""
from gendiff.consts import STATUS, VALUE


def to_string(diff):
    """Func for convert diff to string.

    Args:
        diff: value.

    Returns:
        Value convert in string.
    """
    if diff is None:
        return 'null'

    if isinstance(diff, bool):
        string = str(diff)
        return string.lower()

    return diff


def render_stylish(diff, indent=0):
    """Render diff in stylish format.

    Args:
        diff: Dictionary with the diff result rows.
        indent: indent in line.

    Returns:
        String of diff rows, formatted as a stylish.
    """
    if not isinstance(diff, diff):
        return to_string(diff)

    step = ' ' * indent
    result_render = ['{']

    if indent == 0:
        keys = sorted(diff.keys())
    else:
        keys = diff.keys()

    indent = indent + 4

    for key in keys:
        if diff[key][STATUS] == 'added':
            string = '{0}  + {1}: {2}'.format(step, key, render_stylish(
                diff[key][VALUE],
                indent,
            ),
            )
        if diff[key][STATUS] == 'deleted':
            string = '{0}  - {1}: {2}'.format(step, key, render_stylish(
                diff[key][VALUE],
                indent,
            ),
            )
        if diff[key][STATUS] == 'unchanged':
            string = '{0}    {1}: {2}'.format(step, key, render_stylish(
                diff[key][VALUE],
                indent,
            ),
            )
        if diff[key][STATUS] == 'replaced':
            string = '{0}  - {1}: {2}\n{3}  + {4}: {5}'.format(
                step,
                key,
                render_stylish(diff[key][VALUE], indent),
                step,
                key,
                render_stylish(diff[key]['value2'], indent),
            )
        if diff[key][STATUS] == 'changed':
            string = '{0}    {1}: {2}'.format(step, key, render_stylish(
                diff[key][VALUE],
                indent,
            ),
            )
        result_render.append(string)

    result_render.append('{0}}}'.format(step))
    return '\n'.join(result_render)
