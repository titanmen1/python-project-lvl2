def to_string(diff):
    """
     representation for key values,
     that are not dictionary
    Parameters:
        diff: difference that are not dictionary
    Return:
        string format for 'None" and boolean
        string as string, and numbers
    """
    if diff is None:
        return 'null'

    if type(diff) == bool:
        string = str(diff)
        return string.lower()

    return diff


def render_stylish(diff, indent=0):

    if type(diff) != dict:
        return to_string(diff)

    step = ' ' * indent
    result = ['{']

    if indent == 0:
        keys = sorted(diff.keys())
    else:
        keys = diff.keys()

    indent = indent + 4

    for key in keys:
        if diff[key]['status'] == 'added':
            string = "{0}  + {1}: {2}".format(step, key, render_stylish(diff[key]['value'], indent))
        if diff[key]['status'] == 'deleted':
            string = "{0}  - {1}: {2}".format(step, key, render_stylish(diff[key]['value'], indent))
        if diff[key]['status'] == 'unchanged':
            string = "{0}    {1}: {2}".format(step, key, render_stylish(diff[key]['value'], indent))
        if diff[key]['status'] == 'replaced':
            string = "{0}  - {1}: {2}" \
                     "\n{3}  + {4}: {5}"\
                .format(step, key, render_stylish(diff[key]['value'], indent), step, key,
                        render_stylish(diff[key]['value2'], indent))
        if diff[key]['status'] == 'changed':
            string = "{0}    {1}: {2}".format(step, key, render_stylish(diff[key]['value'], indent))
        result.append(string)

    result.append('{0}}}'.format(step))
    return '\n'.join(result)

