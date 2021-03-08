import gendiff.engine.parsers as parsers


def get_plain(diff):
    plain_dict = diff_to_list(diff)
    return '\n'.join(plain_dict)


def diff_to_list(diff, prefix=''):
    res = []
    for key, key_description in diff.items():
        res += parse_key_description(key, key_description, prefix)
    res.sort()
    return res


def parse_key_description(key, key_description, prefix):
    res = []
    if parsers.have_children(key_description):
        children = parsers.get_children(key_description)
        children_keys = diff_to_list(children, get_new_prefix(prefix, key))
        res += children_keys
    else:
        key_status = parsers.get_status(key_description)
        if key_status != parsers.STATUS_STAY:
            value = parsers.get_value(key_description)
            full_key = get_new_prefix(prefix, key)
            res.append('{}\'{}\' {}'.format('Property ', full_key,
                                            format_description(key_status,
                                                               value)))
    return res


def get_new_prefix(prefix, key):
    if not prefix:
        return key
    return '{}.{}'.format(prefix, key)


def format_description(key_status, key_value):
    res = ''
    if key_status == parsers.STATUS_CHANGE:
        res = 'was updated. From {} to {}'.format(
            format_value(key_value[parsers.STATUS_DEL]),
            format_value(key_value[parsers.STATUS_NEW]))
    elif key_status == parsers.STATUS_DEL:
        res = 'was removed'
    elif key_status == parsers.STATUS_NEW:
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
