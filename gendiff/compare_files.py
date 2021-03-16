from gendiff.parsers import parse_files
from gendiff.formatters.formatter_stylish import get_stylish
from gendiff.formatters.formatter_plain import get_plain
from gendiff.formatters.formatter_json import get_json


def generate_diff(file_original, file_modified, out_format='stylish'):
    diff = parse_files(file_original, file_modified)
    res = '{} is {}'.format(out_format, 'unknown format')
    if out_format == 'stylish':
        res = get_stylish(diff)
    if out_format == 'plain':
        res = get_plain(diff)
    if out_format == 'json':
        res = get_json(diff)
    return res
