"""Func for formatting diff in json format."""
import json


def render_json(diff):
    """Func for formatting diff in json format.

    Args:
        diff: diff for render in json format.

    Returns:
        Diff in json format
    """
    return json.dumps(diff, indent=2)
