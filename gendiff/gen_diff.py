from gendiff.out_log import log_info
import gendiff.io as io
import gendiff.parsing as parsing

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

from gendiff.formatters.format import format_diff  # noqa: E402


def generate_diff(file_old, file_new, out_format='stylish'):
    data_old = get_data(file_old)
    data_new = get_data(file_new)

    inner_diff = get_inner_diff(data_old, data_new)
    log_info('inner_diff', inner_diff)
    diff = format_diff(inner_diff, out_format)

    return diff


def get_data(source):
    parser = get_parser(source)
    data = io.load(source)
    if not data:
        raise ValueError('empty data in: {}'.format(source))
    parsed = parser(data)
    return parsed


def get_inner_diff(old_data, new_data, root_key=''):
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
            stay_key = get_inner_diff(old_data[key], new_data[key], key)
        else:
            stay_key = {KEY_KEY: key}
            if old_data[key] == new_data[key]:
                stay_key.update({KEY_STATUS: STATUS_STAY,
                                 KEY_VALUE: {VALUE_STAY: old_data[key]}})
            else:
                stay_key.update({KEY_STATUS: STATUS_CHANGE,
                                 KEY_VALUE: {VALUE_DEL: old_data[key],
                                             VALUE_NEW: new_data[key]}})

        children.append(stay_key)
        children.sort(key=get_key)

    res = {KEY_KEY: root_key,
           KEY_CHILDREN: children}
    return res


def get_key(inner_diff):
    return inner_diff[KEY_KEY]


def get_parser(file_path):
    if '.json' in file_path:
        parser = parsing.parse_json
    elif '.yml' in file_path:
        parser = parsing.parse_yaml
    else:
        raise ValueError('can\'t detect format for: {}'.format(file_path))
    return parser
