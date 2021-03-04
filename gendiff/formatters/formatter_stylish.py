def get_stylish(diff):
    stylish_dict = diff_to_uniform_dict(diff)
    list_data = stylish_to_list(stylish_dict)
    res = '{}\n{}\n{}'.format('{', '\n'.join(list_data), '}')
    return res


def diff_to_uniform_dict(data):
    sorted_keys = sorted(list(data.keys()))
    res = {}
    for key in sorted_keys:
        key_description = data[key]
        children = key_description.get('_CHILDREN_', None)
        if children:
            value = diff_to_uniform_dict(children)
            res[key] = value
        else:
            key_status = key_description['_STATUS_']
            value = key_description['_VALUE_']
            if key_status == '_CHANGE_':
                res[get_stylish_key('_DEL_', key)] = value['_OLD_']
                res[get_stylish_key('_NEW_', key)] = value['_NEW_']
            else:
                res[get_stylish_key(key_status, key)] = value
    return res


def get_stylish_key(status, key):
    sign = {'_DEL_': '-', '_NEW_': '+', '_STAY_': ' '}[status]
    return '{} {}'.format(sign, key)


def stylish_to_list(data, level=2):
    res = []
    shift = ' ' * level
    for key, value in data.items():
        key = format_key(key)
        if isinstance(value, dict):
            res.append('{}{}: {}'.format(shift, key, '{'))
            res = res + stylish_to_list(value, level + 4)
            res.append('{}  {}'.format(shift, '}'))
        else:
            formatted_value = format_value(value)
            res.append('{}{}:{}'.format(shift, key, formatted_value))
    return res


def format_key(key):
    shift = ''
    if ' ' not in key:
        shift = '  '
    return '{}{}'.format(shift, key)


def format_value(value):
    shift = ''
    if value != '':
        shift = ' '
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return '{}{}'.format(shift, value)