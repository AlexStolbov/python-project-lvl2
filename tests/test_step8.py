from os import path
from gendiff.generate_diff import generate_diff
from tests.test_step6 import FIXTURES_DIR_6

FIXTURES_DIR_8 = 'fixtures/step8'


def test_json():
    current_dir = path.dirname(__file__)
    file_old = path.join(current_dir, FIXTURES_DIR_6, 'file1.json')
    file_new = path.join(current_dir, FIXTURES_DIR_6, 'file2.json')
    res_json = generate_diff(file_old, file_new, out_format='json')
    path_should_be = path.join(current_dir, FIXTURES_DIR_8, 'result.json')
    should_be = open(path_should_be).read()
    assert res_json == should_be


if __name__ == '__main__':
    test_json()
