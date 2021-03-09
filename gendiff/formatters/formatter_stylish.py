from operator import itemgetter
import gendiff.engine.parsers as parsers


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
    if parsers.have_children(key_description):
        children = parsers.get_children(key_description)
        value = diff_to_uniform_dict(children)
        res[parsers.STATUS_STAY, key] = value
    else:
        key_status = parsers.get_status(key_description)
        value = parsers.get_value(key_description)
        if key_status == parsers.STATUS_CHANGE:
            res[parsers.STATUS_DEL, key] = value[parsers.STATUS_DEL]
            res[parsers.STATUS_NEW, key] = value[parsers.STATUS_NEW]
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
        sign = {parsers.STATUS_DEL: '-',
                parsers.STATUS_NEW: '+',
                parsers.STATUS_STAY: ' '}[key[0]]
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
