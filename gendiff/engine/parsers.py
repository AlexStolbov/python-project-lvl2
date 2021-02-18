import json
import yaml


def parse_files(origin_file, modified_file):
    """
    Runs load file and runs parser
    Return parser's result
    """
    origin_data = load_file(origin_file)
    modified_data = load_file(modified_file)
    parse_result = {}
    if origin_data is not None and modified_data is not None:
        parse_result = parse_data(origin_data, modified_data)
    return parse_result


def load_file(file_path):
    """
    Load json or yaml file
    """
    def is_json(file_name):
        """
        Simple check
        """
        return '.json' in file_name

    def is_yaml(file_name):
        """
        Simple check
        """
        return '.yml' in file_name

    if is_json(file_path):
        return json.load(open(file_path))
    elif is_yaml(file_path):
        return yaml.safe_load(open(file_path))
    else:
        return None


def parse_data(origin_data,  modified_data):
    origin_keys = list(origin_data.keys())
    modified_keys = list(modified_data.keys())
    all_keys = set(origin_keys + modified_keys)
    res = {}
    for key in all_keys:
        if key not in origin_keys:
            res[key] = [{'added': '+', 'value': modified_data[key]}]
        elif key not in modified_keys:
            res[key] = [{'added': '-', 'value': origin_data[key]}]
        elif origin_data[key] == modified_data[key]:
            res[key] = [{'added': ' ', 'value': origin_data[key]}]
        else:
            res[key] = [{'added': '-', 'value': origin_data[key]},
                        {'added': '+', 'value': modified_data[key]}, ]
    return res
