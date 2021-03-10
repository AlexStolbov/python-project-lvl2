import json
import yaml

KEY_NAME = '_KEY_NAME_'
KEY_STATUS = '_KEY_STATUS_'
KEY_VALUE = '_KEY_VALUE_'
KEY_CHILDREN = '_KEY_CHILDREN_'
STATUS_NEW = '_NEW_'
STATUS_DEL = '_DEL_'
STATUS_STAY = '_STAY_'
STATUS_CHANGE = '_CHANGE_'


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
    res = {}
    del_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    res.update(add_new_or_del_keys(old_data, del_keys - new_keys, STATUS_DEL))
    res.update(add_new_or_del_keys(new_data, new_keys - del_keys, STATUS_NEW))
    res.update(add_stay_keys(old_data, new_data, del_keys & new_keys))
    return res


def add_new_or_del_keys(data, keys, key_status):
    res = {}
    for key in keys:
        res[key] = make_key_description(key_status=key_status,
                                        key_value=data[key])
    return res


def add_stay_keys(old_data, new_data, keys):
    res = {}
    for key in keys:
        if isinstance(old_data[key], dict) and isinstance(new_data[key], dict):
            res[key] = get_node(old_data, new_data, key)
        else:
            res[key] = get_simple_key(old_data, new_data, key)
    return res


def get_node(old_data, new_data, key):
    children = parse_data(old_data[key], new_data[key])
    res = make_key_description(children=children)
    return res


def get_simple_key(old_data, new_data, key):
    old_value = old_data[key]
    new_value = new_data[key]
    if old_value == new_value:
        res = make_key_description(key_status=STATUS_STAY,
                                   key_value=old_value)
    else:
        res = make_key_description(key_status=STATUS_CHANGE,
                                   key_value={STATUS_DEL: old_value,
                                              STATUS_NEW: new_value})
    return res


def make_key_description(key_status=None, key_value=None, children=None):
    res = {}
    if key_status is not None:
        res[KEY_STATUS] = key_status
    if key_value is not None:
        res[KEY_VALUE] = key_value
    if children is not None:
        res[KEY_CHILDREN] = children
    return res


def get_status(key_description):
    return key_description[KEY_STATUS]


def get_value(key_description):
    return key_description[KEY_VALUE]


def get_children(key_description):
    return key_description[KEY_CHILDREN]


def have_children(key_description):
    return KEY_CHILDREN in key_description
