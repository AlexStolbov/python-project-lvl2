from operator import itemgetter
import gendiff.gendiff as generate_diff


def get_stylish(diff):
    stylish_dict = diff_to_uniform_dict(diff)
    list_data = stylish_to_list(stylish_dict)
    res = '{}\n{}\n{}'.format('{', '\n'.join(list_data), '}')
    return res


def diff_to_uniform_dict(diff):
    res = {}
    for key, key_description in diff.items():
        res.update(parse_key_description(key, key_description))
    return res


def parse_key_description(key, key_description):
    res = {}
    if generate_diff.KEY_CHILDREN in key_description:
        children = key_description[generate_diff.KEY_CHILDREN]
        value = diff_to_uniform_dict(children)
        res[generate_diff.STATUS_STAY, key] = value
    else:
        key_status = key_description[generate_diff.KEY_STATUS]
        value = key_description[generate_diff.KEY_VALUE]
        if key_status == generate_diff.STATUS_CHANGE:
            res[generate_diff.STATUS_DEL, key] = value[generate_diff.STATUS_DEL]
            res[generate_diff.STATUS_NEW, key] = value[generate_diff.STATUS_NEW]
        else:
            res[key_status, key] = value
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
            formatted_value = format_value(value)
            res.append('{}{}:{}'.format(shift, formatted_key, formatted_value))
    return res


def format_key(key):
    if isinstance(key, tuple):
        sign = {generate_diff.STATUS_DEL: '-',
                generate_diff.STATUS_NEW: '+',
                generate_diff.STATUS_STAY: ' '}[key[0]]
        key_single = key[1]
    else:
        sign = ' '
        key_single = key
    return '{} {}'.format(sign, key_single)


def format_value(value):
    shift = ' '
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return '{}{}'.format(shift, value)
