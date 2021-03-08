from gendiff.scripts.gendiff_script import generate_diff
from os import path

FIXTURES_DIR_4 = 'fixtures/step4'


def test_gendiff():
    current_dir = path.dirname(__file__)
    path_origin = path.join(current_dir, FIXTURES_DIR_4, 'lvl2_original.json')
    path_modified = path.join(current_dir, FIXTURES_DIR_4, 'lvl2_modified.json')
    path_should_be = path.join(current_dir, FIXTURES_DIR_4, 'should_be.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


if __name__ == '__main__':
    test_gendiff()
