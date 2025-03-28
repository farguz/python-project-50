import json


def json_format(diff_tree: dict) -> str:
    return json.dumps(diff_tree)
