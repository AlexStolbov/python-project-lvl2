from os import path
from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff

CURRENT_DIR = path.dirname(__file__)
FIXTURES_DIR = 'fixtures'
PLAIN_JSON_DIR = path.join(FIXTURES_DIR, 'plain_json')
PLAIN_YML_DIR = path.join(FIXTURES_DIR, 'plain_yaml')
NESTED_JSON_DIR = path.join(FIXTURES_DIR, 'nested_json')
NESTED_YML_DIR = path.join(FIXTURES_DIR, 'nested_yml')


def path_current(*paths):
    return path.join(CURRENT_DIR, *paths)


def test_plain_json():
    path_origin = path_current(PLAIN_JSON_DIR, 'plain_original.json')
    path_modified = path_current(PLAIN_JSON_DIR, 'plain_modified.json')
    path_diff = path_current(FIXTURES_DIR, 'stylish_plain_diff.txt')
    res = generate_diff(path_origin, path_modified)
    diff = open(path_diff).read()
    assert res == diff


def test_plain_yaml():
    path_origin = path_current(PLAIN_YML_DIR, 'plain_original.yml')
    path_modified = path_current(PLAIN_YML_DIR, 'plain_modified.yml')
    path_diff = path_current(FIXTURES_DIR, 'stylish_plain_diff.txt')
    res = generate_diff(path_origin, path_modified)
    diff = open(path_diff).read()
    assert res == diff


def test_nested_json():
    path_origin = path_current(NESTED_JSON_DIR, 'nested_original.json')
    path_modified = path_current(NESTED_JSON_DIR, 'nested_modified.json')
    path_diff = path_current(FIXTURES_DIR, 'stylish_nested_diff.txt')
    res = generate_diff(path_origin, path_modified)
    diff = open(path_diff).read()
    assert res == diff


def test_nested_yaml():
    path_origin = path_current(NESTED_YML_DIR, 'nested_original.yml')
    path_modified = path_current(NESTED_YML_DIR, 'nested_modified.yml')
    path_diff = path_current(FIXTURES_DIR, 'stylish_nested_diff.txt')
    res = generate_diff(path_origin, path_modified)
    diff = open(path_diff).read()
    assert res == diff


def test_plain():
    path_origin = path_current(NESTED_JSON_DIR, 'nested_original.json')
    path_modified = path_current(NESTED_JSON_DIR, 'nested_modified.json')
    path_diff = path_current(FIXTURES_DIR, 'plain_diff.txt')
    res = generate_diff(path_origin, path_modified, out_format='plain')
    diff = open(path_diff).read()
    assert res == diff


def test_parse_args():
    params = {'first_file': 'file1',
              'second_file': 'file2',
              'format': 'stylish'}
    args = parse_args(['--format', params['format'],
                       params['first_file'],
                       params['second_file']])
    args_dict = vars(args)
    assert params == args_dict


def test_json_diff():
    path_origin = path_current(NESTED_JSON_DIR, 'nested_original.json')
    path_modified = path_current(NESTED_JSON_DIR, 'nested_modified.json')
    path_diff = path_current(FIXTURES_DIR, 'json_diff.json')
    res = generate_diff(path_origin, path_modified, out_format='json')
    diff = open(path_diff).read()
    assert res == diff


if __name__ == '__main__':
    test_nested_yaml()
