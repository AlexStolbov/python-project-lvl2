from os import path
import pytest
from gendiff.cli import parse_args
from gendiff.gen_diff import generate_diff
import json

CURRENT_DIR = path.dirname(__file__)
PLAIN_JSON_DIR = 'plain_json'
PLAIN_YML_DIR = 'plain_yaml'
NESTED_JSON_DIR = 'nested_json'
NESTED_YML_DIR = 'nested_yml'


def path_current(*paths):
    return path.join(CURRENT_DIR, 'fixtures', *paths)


SET_TESTING_DATA = [
    (PLAIN_JSON_DIR, 'plain_original.json', 'plain_modified.json',
     'stylish_plain_diff.txt', 'stylish'),
    (PLAIN_YML_DIR, 'plain_original.yml', 'plain_modified.yml',
     'stylish_plain_diff.txt', 'stylish'),
    (NESTED_JSON_DIR, 'nested_original.json', 'nested_modified.json',
     'stylish_nested_diff.txt', 'stylish'),
    (NESTED_YML_DIR, 'nested_original.yml', 'nested_modified.yml',
     'stylish_nested_diff.txt', 'stylish'),
    (NESTED_JSON_DIR, 'nested_original.json', 'nested_modified.json',
     'plain_diff.txt', 'plain')]


@pytest.mark.parametrize(
    'files_dir, path_origin, path_modified, path_diff, out_format',
    SET_TESTING_DATA)
def test_gendiff(files_dir, path_origin, path_modified, path_diff,
                 out_format):
    res = generate_diff(path_current(files_dir, path_origin),
                        path_current(files_dir, path_modified),
                        out_format)
    diff = open(path_current(path_diff)).read()
    assert res == diff


def test_gendiff_unknown_format():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'plain_original.json'),
            path_current(PLAIN_JSON_DIR, 'plain_modified.json'),
            'unknown_format')


def test_gendiff_skipped_one_file():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'plain_original.json'),
            '')


def test_gendiff_empty_file():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'plain_original.json'),
            path_current('empty.json'))
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'plain_original.json'),
            path_current('empty.yml'))


def test_format_json():
    res = generate_diff(path_current(NESTED_JSON_DIR, 'nested_original.json'),
                        path_current(NESTED_JSON_DIR, 'nested_modified.json'),
                        'json')
    j1 = json.loads(res)
    j2 = json.load(open(path_current('json_diff.json')))
    assert j1 == j2


def test_parse_args():
    params = {'first_file': 'file1',
              'second_file': 'file2',
              'format': 'stylish'}
    args = parse_args(['--format', params['format'],
                       params['first_file'],
                       params['second_file']])
    args_dict = vars(args)
    assert params == args_dict
