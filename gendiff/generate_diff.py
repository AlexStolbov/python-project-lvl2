from gendiff.open_source import open_source
from gendiff.parse_source import parse
from gendiff.formatters.make_format import make_format

KEY_NAME = '_KEY_NAME_'
KEY_STATUS = '_KEY_STATUS_'
KEY_VALUE = '_KEY_VALUE_'
KEY_CHILDREN = '_KEY_CHILDREN_'
STATUS_NEW = '_NEW_'
STATUS_DEL = '_DEL_'
STATUS_STAY = '_STAY_'
STATUS_CHANGE = '_CHANGE_'


def generate_diff(file_old, file_new, out_format='stylish'):
    data_source_old, format_old = open_source(file_old)
    data_source_new, format_new = open_source(file_new)

    data_old = parse(data_source_old, format_old)
    data_new = parse(data_source_new, format_new)

    diff = []
    if data_old is not None and data_new is not None:
        inner_diff = compare_data(data_old, data_new)
        diff = make_format(inner_diff, out_format)

    return diff


def compare_data(old_data, new_data):
    res = {}
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    all_keys = old_keys | new_keys
    for key in all_keys:
        if key not in old_keys:
            res[key] = make_key_description(key_status=STATUS_NEW,
                                            key_value=new_data[key])
        elif key not in new_keys:
            res[key] = make_key_description(key_status=STATUS_DEL,
                                            key_value=old_data[key])
        else:
            if isinstance(old_data[key], dict) and isinstance(new_data[key],
                                                              dict):
                res[key] = get_node(old_data, new_data, key)
            else:
                res[key] = get_simple_key(old_data, new_data, key)
    return res


def get_node(old_data, new_data, key):
    children = compare_data(old_data[key], new_data[key])
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
