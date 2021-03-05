from os import path
from tests.test_step7 import get_diff_from_json
from gendiff.formatters.formatter_json import get_json

FIXTURES_DIR_8 = 'fixtures/step8'


def test_json():
    diff = get_diff_from_json()
    # print(diff)
    res_json = get_json(diff)
    current_dir = path.dirname(__file__)
    path_should_be = path.join(current_dir, FIXTURES_DIR_8, 'result.json')
    should_be = open(path_should_be).read()
    # print(res_json)
    # print(should_be)
    assert res_json == should_be


if __name__ == '__main__':
    test_json()
