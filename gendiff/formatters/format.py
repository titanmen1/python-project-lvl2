"""Func select type formatting."""
from gendiff.formatters.json import render_json
from gendiff.formatters.plain import render_plain
from gendiff.formatters.stylish import render_stylish


def format_diff(diff, format_name):
    """Func select type formatting.

    Args:
        diff: diff for render some format.
        format_name: format type

    Returns:
        Diff in selected format
    """
    if format_name == 'json':
        return render_json(diff)
    if format_name == 'plain':
        return render_plain(diff)
    if format_name == 'stylish':
        return render_stylish(diff)
