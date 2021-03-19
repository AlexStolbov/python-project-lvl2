from os import path
from gendiff import generate_diff
from tests.test_step6 import FIXTURES_DIR_6

FIXTURES_DIR_7 = 'fixtures/step7'


def test_plain():
    current_dir = path.dirname(__file__)
    file_old = path.join(current_dir, FIXTURES_DIR_6, 'file1.json')
    file_new = path.join(current_dir, FIXTURES_DIR_6, 'file2.json')
    plain = generate_diff(file_old, file_new, out_format='plain')
    print(plain)
    path_should_be = path.join(current_dir, FIXTURES_DIR_7, 'plain.txt')
    should_be = open(path_should_be).read()
    assert plain == should_be


if __name__ == '__main__':
    test_plain()
