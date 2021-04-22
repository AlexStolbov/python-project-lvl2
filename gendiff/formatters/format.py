from gendiff.formatters.formatter_stylish import get_stylish
from gendiff.formatters.formatter_plain import get_plain
from gendiff.formatters.formatter_json import get_json


def format_diff(inner_diff, out_format):
    if out_format == 'stylish':
        diff = get_stylish(inner_diff)
    elif out_format == 'plain':
        diff = get_plain(inner_diff)
    elif out_format == 'json':
        diff = get_json(inner_diff)
    else:
        raise ValueError('{} is unknown format'.format(out_format))
    return diff
