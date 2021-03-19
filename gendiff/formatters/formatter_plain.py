import gendiff.generate_diff as generate_diff


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
    if generate_diff.have_children(key_description):
        children = generate_diff.get_children(key_description)
        children_keys = diff_to_list(children, get_new_prefix(prefix, key))
        res += children_keys
    else:
        key_status = generate_diff.get_status(key_description)
        if key_status != generate_diff.STATUS_STAY:
            value = generate_diff.get_value(key_description)
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
    if key_status == generate_diff.STATUS_CHANGE:
        res = 'was updated. From {} to {}'.format(
            format_value(key_value[generate_diff.STATUS_DEL]),
            format_value(key_value[generate_diff.STATUS_NEW]))
    elif key_status == generate_diff.STATUS_DEL:
        res = 'was removed'
    elif key_status == generate_diff.STATUS_NEW:
        res = 'was added with value: {}'.format(format_value(key_value))
    return res


def format_value(value):
    if isinstance(value, dict):
        res = '[complex value]'
    elif isinstance(value, str):
        res = '\'{}\''.format(value)
    elif value in (True, False, None):
        res = {True: 'true', False: 'false', None: 'null'}[value]
    else:
        res = value
    return res
