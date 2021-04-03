KEY_STATUS = '_STATUS_'
KEY_VALUE = '_VALUE_'
KEY_CHILDREN = '_CHILDREN_'
STATUS_STAY = '_STAY_'
STATUS_DEL = '_DEL_'
STATUS_NEW = '_NEW_'
STATUS_CHANGE = '_CHANGE_'
VALUE_STAY = '_STAY_'
VALUE_DEL = '_DEL_'
VALUE_NEW = '_NEW_'


def compare_data(old_data, new_data):
    res = {}
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    for key in new_keys - old_keys:
        res[key] = {KEY_STATUS: STATUS_NEW,
                    KEY_VALUE: {VALUE_NEW: new_data[key]}}
    for key in old_keys - new_keys:
        res[key] = {KEY_STATUS: STATUS_DEL,
                    KEY_VALUE: {VALUE_DEL: old_data[key]}}
    for key in old_keys & new_keys:
        if isinstance(old_data[key], dict) and isinstance(new_data[key],
                                                          dict):
            res[key] = get_node(old_data, new_data, key)
        else:
            res[key] = get_simple_key(old_data[key], new_data[key])
    return res


def get_node(old_data, new_data, key):
    children = compare_data(old_data[key], new_data[key])
    res = {KEY_CHILDREN: children}
    return res


def get_simple_key(old_value, new_value):
    if old_value == new_value:
        res = {KEY_STATUS: STATUS_STAY,
               KEY_VALUE: {VALUE_STAY: old_value}}
    else:
        res = {KEY_STATUS: STATUS_CHANGE,
               KEY_VALUE: {VALUE_DEL: old_value, VALUE_NEW: new_value}}
    return res
