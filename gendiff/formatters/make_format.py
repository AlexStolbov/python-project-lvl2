from gendiff.formatters.formatter_stylish import get_stylish
from gendiff.formatters.formatter_plain import get_plain
from gendiff.formatters.formatter_json import get_json


def make_format(inner_diff, out_format):
    diff = '{} is {}'.format(out_format, 'unknown format')
    if out_format == 'stylish':
        diff = get_stylish(inner_diff)
    if out_format == 'plain':
        diff = get_plain(inner_diff)
    if out_format == 'json':
        diff = get_json(inner_diff)
    return diff
