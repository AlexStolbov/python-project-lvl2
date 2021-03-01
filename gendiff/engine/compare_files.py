from gendiff.engine.parsers import parse_files
from gendiff.engine.stylish import stylish


def generate_diff(file_original, file_modified, out_format='stylish'):
    diff = parse_files(file_original, file_modified)
    res = '{} is {}'.format(out_format, 'unknown format')
    if out_format == 'stylish':
        res = stylish(diff)
    return res
