"""Func for formatting diff in stylish format."""
from gendiff.consts import STATUS, VALUE

INDENT_TYPE = " "
INDENT_SIZE = 4


def stringify(value, depth):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        result = []
        indent = make_indent(depth + 1)
        for key, value in value.items():
            str_value = stringify(value, depth + 1)
            result.append(
                f'{indent}    {key}: {str_value}\n')
        return f'{{\n{"".join(result)}{indent}}}'

    return value


def make_indent(depth, indent_size=INDENT_SIZE, indent_type=INDENT_TYPE):
    return indent_type * indent_size * depth


def render_stylish(diff, depth=0):
    """Render diff in stylish format.

    Args:
        diff: Dictionary with the diff result rows.
        indent: indent in line.

    Returns:
        String of diff rows, formatted as a stylish.
    """
    diff_type = diff["type"]
    key = diff.get("key")
    indent = make_indent(depth)
    children = diff.get('children')

    if diff_type == "origin":
        rows = [f'{indent}{render_stylish(child, depth)}\n' for child in children]
        return f'{{\n{"".join(rows)}}}'

    if diff_type == "nested":
        rows = [f'{render_stylish(child, depth + 1)}\n' for child in children]
        result = "".join(rows)
        return (
            f'{indent}    {key}: {{\n{result}{make_indent(depth + 1)}}}'
        )

    if diff_type == "added":
        return (
            f'{indent}  + {key}: {stringify(diff["value"], depth)}'
        )

    if diff_type == "removed":
        return (
            f'{indent}  - {key}: {stringify(diff["value"], depth)}'
        )

    if diff_type == "updated":
        return '\n'.join([
            f'{indent}  - {key}: {stringify(diff["old_value"], depth)}',
            f'{indent}  + {key}: {stringify(diff["new_value"], depth)}'
        ])

    if diff_type == "unchanged":
        return (
            f'{indent}    {key}: {stringify(diff["value"], depth)}'
        )
