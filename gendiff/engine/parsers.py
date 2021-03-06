import json
import yaml


def parse_files(origin_file, modified_file):
    """
    Runs load file and runs parser
    Return parser's result
    """
    origin_data = load_file(origin_file)
    modified_data = load_file(modified_file)
    parse_result = []
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


def parse_data(old_data, new_data):
    res = []
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    res += add_new_or_del_keys(old_data, old_keys - new_keys, '_DEL_')
    res += add_new_or_del_keys(new_data, new_keys - old_keys, '_NEW_')
    res += add_stay_keys(old_data, new_data, old_keys & new_keys)
    return res


def add_new_or_del_keys(data, keys, key_status):
    res = []
    for key in keys:
        res.append(make_key_description(key=key,
                                        key_status=key_status,
                                        key_value=data[key]))
    return res


def add_stay_keys(old_data, new_data, keys):
    res = []
    for key in keys:
        if isinstance(old_data[key], dict) and isinstance(new_data[key], dict):
            res.append(get_node(old_data, new_data, key))
        else:
            res.append(get_simple_key(old_data, new_data, key))
    return res


def get_node(old_data, new_data, key):
    children = parse_data(old_data[key], new_data[key])
    res = make_key_description(key=key,
                               children=children)
    return res


def get_simple_key(old_data, new_data, key):
    old_value = old_data[key]
    new_value = new_data[key]
    if old_value == new_value:
        res = make_key_description(key=key,
                                   key_status='_STAY_',
                                   key_value=old_value)
    else:
        res = make_key_description(key=key,
                                   key_status='_CHANGE_',
                                   key_value={'_OLD_': old_value,
                                              '_NEW_': new_value})
    return res


def make_key_description(key, key_status=None, key_value=None, children=None):
    res = {'_KEY_': key}
    if key_status is not None:
        res['_STATUS_'] = key_status
    if key_value is not None:
        res['_VALUE_'] = key_value
    if children is not None:
        res['_CHILDREN_'] = children
    return res
