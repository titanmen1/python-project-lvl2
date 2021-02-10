"""Func for formatting diff in plain format."""
from gendiff.consts import STATUS, VALUE

def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    if value is None:
        return "null"

    return str(value).lower()


def flat_list(items):
    flatten_rows = []

    if type(items) != list:
        return [items]
    for item in items:
        flatten_rows.extend(flat_list(item))

    return flatten_rows


def render_plain(diff):
    diff_type = diff["type"]
    key = diff.get("key")
    children = diff.get("children")

    if diff_type == 'origin':
        rows = [format(child) for child in children]
        return '\n'.join(flat_list(rows))

    if diff_type == "nested":
        rows = []
        for child in children:
            child["key"] = f'{key}.{child["key"]}'
            rows.append(format(child))
        return rows

    if diff_type == "added":
        value = stringify(diff['value'])
        return (
            f"Property '{key}' was added with value: {value}"
        )

    if diff_type == "removed":
        return f"Property '{key}' was removed"

    if diff_type == "updated":
        value = stringify(diff['old_value'])
        new_value = stringify(diff['new_value'])
        return (
            f"Property '{key}' was updated. From {value} to {new_value}"
        )

    if diff_type == "unchanged":
        return []