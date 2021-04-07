from operator import itemgetter
from gendiff.logout import log_info
import gendiff.make_inner_diff as inner_diff


def get_stylish(diff):
    stylish_dict = diff_to_uniform_dict(diff)
    log_info('stylish_uniform', stylish_dict)
    list_data = stylish_to_list(stylish_dict)
    res = '{}\n{}\n{}'.format('{', '\n'.join(list_data), '}')
    log_info('stylish_json', res)
    return res


def diff_to_uniform_dict(diff):
    res = {}
    current_key = diff[inner_diff.KEY_KEY]

    if inner_diff.KEY_CHILDREN not in diff:
        for status, value in diff[inner_diff.KEY_VALUE].items():
            res[status, current_key] = value
        return res

    for child in diff[inner_diff.KEY_CHILDREN]:
        res.update(diff_to_uniform_dict(child))

    if current_key:
        res = {(inner_diff.VALUE_STAY, current_key): res}

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
        sign = {inner_diff.VALUE_DEL: '-',
                inner_diff.VALUE_NEW: '+',
                inner_diff.VALUE_STAY: ' '}[key[0]]

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
