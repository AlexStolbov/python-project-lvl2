import json
from gendiff.out_log import log_info


def get_json(diff):
    res = json.dumps(diff, indent=2, sort_keys=True)
    log_info('formatter json', res)
    return res
