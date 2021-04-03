from operator import itemgetter
from gendiff.logout import log_info
import gendiff.make_inner_diff as make_inner_diff


def get_stylish(diff):
    stylish_dict = diff_to_uniform_dict(diff)
    log_info('stylish_uniform', stylish_dict)
    list_data = stylish_to_list(stylish_dict)
    res = '{}\n{}\n{}'.format('{', '\n'.join(list_data), '}')
    log_info('stylish_json', res)
    return res


def diff_to_uniform_dict(diff):
    res = {}
    for key, key_description in diff.items():
        res.update(parse_key_description(key, key_description))
    return res


def parse_key_description(key, key_description):
    res = {}
    if make_inner_diff.KEY_CHILDREN in key_description:
        children = key_description[make_inner_diff.KEY_CHILDREN]
        value = diff_to_uniform_dict(children)
        res[make_inner_diff.VALUE_STAY, key] = value
    else:
        values = key_description[make_inner_diff.KEY_VALUE]
        for value_status, value in values.items():
            res[value_status, key] = value
    return res


def stylish_to_list(data, level=2):
    res = []
    shift = ' ' * level
    sorted_keys = sorted(list(data.keys()), key=itemgetter(1))
    for key in sorted_keys:
        value = data[key]
        formatted_key = format_key(key)
        if isinstance(value, dict):
            res.append('{}{}: {}'.format(shift, formatted_key, '{'))
            res = res + stylish_to_list(value, level + 4)
            res.append('{}  {}'.format(shift, '}'))
        else:
            formatted_value = to_string(value)
            res.append('{}{}:{}'.format(shift, formatted_key, formatted_value))
    return res


def format_key(key):
    if isinstance(key, tuple):
        sign = {make_inner_diff.VALUE_DEL: '-',
                make_inner_diff.VALUE_NEW: '+',
                make_inner_diff.VALUE_STAY: ' '}[key[0]]

        key_single = key[1]
    else:
        sign = ' '
        key_single = key
    return '{} {}'.format(sign, key_single)


def to_string(value):
    shift = ' '
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return '{}{}'.format(shift, value)
