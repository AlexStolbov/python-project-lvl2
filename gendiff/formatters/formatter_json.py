import json


def get_json(diff):
    res = json.dumps(diff, indent=2, sort_keys=True)
    return res
