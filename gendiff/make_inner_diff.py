KEY_KEY = '_KEY_'
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


def compare_data(old_data, new_data, root_key=''):
    children = []
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    for key in new_keys - old_keys:
        children.append({KEY_KEY: key,
                         KEY_STATUS: STATUS_NEW,
                         KEY_VALUE: {VALUE_NEW: new_data[key]}})
    for key in old_keys - new_keys:
        children.append({KEY_KEY: key,
                         KEY_STATUS: STATUS_DEL,
                         KEY_VALUE: {VALUE_DEL: old_data[key]}})
    for key in old_keys & new_keys:
        if isinstance(old_data[key], dict) and isinstance(new_data[key],
                                                          dict):
            children.append(compare_data(old_data[key], new_data[key], key))

        else:
            children.append(get_simple_key(key, old_data[key], new_data[key]))
        children.sort(key=get_key)

    res = {KEY_KEY: root_key,
           KEY_CHILDREN: children}
    return res


def get_key(inner_diff):
    return inner_diff[KEY_KEY]


def get_simple_key(key, old_value, new_value):
    res = {KEY_KEY: key}
    if old_value == new_value:
        res.update({KEY_STATUS: STATUS_STAY,
                    KEY_VALUE: {VALUE_STAY: old_value}})
    else:
        res.update({KEY_STATUS: STATUS_CHANGE,
                    KEY_VALUE: {VALUE_DEL: old_value, VALUE_NEW: new_value}})
    return res
