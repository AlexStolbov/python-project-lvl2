from os import path
from gendiff.engine.parsers import parse_files
from gendiff.formatters.formatter_plain import get_plain
from tests.test_step6 import FIXTURES_DIR_6

FIXTURES_DIR_7 = 'fixtures/step7'


def get_diff_from_json():
    current_dir = path.dirname(__file__)
    file_original = path.join(current_dir, FIXTURES_DIR_6, 'file1.json')
    file_modified = path.join(current_dir, FIXTURES_DIR_6, 'file2.json')
    diff = parse_files(file_original, file_modified)
    # print(diff)
    return diff


def test_plain():
    current_dir = path.dirname(__file__)
    diff = get_diff_from_json()
    plain = get_plain(diff)
    # print(plain)
    path_should_be = path.join(current_dir, FIXTURES_DIR_7, 'plain.txt')
    should_be = open(path_should_be).read()
    assert plain == should_be


if __name__ == '__main__':
    test_plain()
