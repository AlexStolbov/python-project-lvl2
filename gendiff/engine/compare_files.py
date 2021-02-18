
from gendiff.engine.parsers import parse_files


def generate_diff(file_original, file_modified):
    parse_result = parse_files(file_original, file_modified)
    all_keys = sorted(list(parse_result.keys()))
    res = []
    for key in all_keys:
        for change in parse_result[key]:
            res.append('{} {}: {}'.format(change['added'], key, change['value']))
    return '{}\n{}\n{}'.format('{', '\n'.join(res), '}')


