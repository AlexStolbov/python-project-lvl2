from hexlet_python_package.scripts.gendiff import generate_diff
import os.path

FIXTURES_DIR = 'tests/fixtures/step3'


def test_gendiff():
    path_origin = os.path.join(FIXTURES_DIR, 'lvl2_original.json')
    path_modified = os.path.join(FIXTURES_DIR, 'lvl2_modified.json')
    path_should_be = os.path.join(FIXTURES_DIR, 'should_be.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


if __name__ == '__main__':
    test_gendiff()
