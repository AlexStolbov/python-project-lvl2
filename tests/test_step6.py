from os import path
from gendiff.scripts.gendiff_script import generate_diff, parse_args

FIXTURES_DIR_6 = 'fixtures/step6'


def test_parse_args():
    params = {'first_file': 'file1',
              'second_file': 'file2',
              'format': 'stylish'}
    args = parse_args(['--format', params['format'],
                       params['first_file'],
                       params['second_file']])
    args_dict = vars(args)
    assert params == args_dict


def test_gendiff_json():
    current_dir = path.dirname(__file__)
    path_origin = path.join(current_dir, FIXTURES_DIR_6, 'file1.json')
    path_modified = path.join(current_dir, FIXTURES_DIR_6, 'file2.json')
    path_should_be = path.join(current_dir, FIXTURES_DIR_6, 'compared.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


def test_gendiff_yaml():
    current_dir = path.dirname(__file__)
    path_origin = path.join(current_dir, FIXTURES_DIR_6, 'file1.yml')
    path_modified = path.join(current_dir, FIXTURES_DIR_6, 'file2.yml')
    path_should_be = path.join(current_dir, FIXTURES_DIR_6, 'compared.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


if __name__ == '__main__':
    test_gendiff_json()
    # test_gendiff_yaml()
    # test_parse_args()
