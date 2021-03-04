def get_plain(diff):
    plain_dict = diff_to_list(diff)
    return '\n'.join(plain_dict)


def diff_to_list(data, prefix=''):
    res = []
    for key in data.keys():
        key_description = data[key]
        children = key_description.get('_CHILDREN_', None)
        if children:
            children_keys = diff_to_list(children,
                                         prefix='{}{}.'.format(prefix, key))
            res += children_keys
        else:
            key_status = key_description['_STATUS_']
            if key_status != '_STAY_':
                value = key_description['_VALUE_']
                full_key = '{}{}'.format(prefix, key)
                res.append('{}\'{}\' {}'.format('Property ', full_key,
                                                format_description(key_status,
                                                                   value)))
    res.sort()
    return res


def format_description(key_status, key_value):
    res = ''
    if key_status == '_CHANGE_':
        res = 'was updated. From {} to {}'.format(
            format_value(key_value['_OLD_']),
            format_value(key_value['_NEW_']))
    elif key_status == '_DEL_':
        res = 'was removed'
    elif key_status == '_NEW_':
        res = 'was added with value: {}'.format(format_value(key_value))
    return res


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return '\'{}\''.format(value)
