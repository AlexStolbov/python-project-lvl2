from gendiff.logout import log_info
import gendiff.make_inner_diff as make_inner_diff

DESCR_TEMPLATE = {
    make_inner_diff.STATUS_CHANGE: 'was updated. From {_DEL_} to {_NEW_}',
    make_inner_diff.STATUS_DEL: 'was removed',
    make_inner_diff.STATUS_NEW: 'was added with value: {_NEW_}'}


def get_plain(diff):
    plain_dict = diff_to_list(diff)
    res = '\n'.join(plain_dict)
    log_info('plain diff', res)
    return res


def diff_to_list(diff, prefix=''):
    res = []
    for key, key_description in diff.items():
        res += parse_key_description(key, key_description, prefix)
    res.sort()
    return res


def parse_key_description(key, key_description, prefix):
    res = []

    if make_inner_diff.KEY_CHILDREN in key_description:
        children = key_description[make_inner_diff.KEY_CHILDREN]
        children_keys = diff_to_list(children, get_new_prefix(prefix, key))
        res += children_keys
    else:
        formatted_values = {k: to_string(v) for k, v in
                            key_description[make_inner_diff.KEY_VALUE].items()}

        full_key = get_new_prefix(prefix, key)
        descr = DESCR_TEMPLATE.get(key_description[make_inner_diff.KEY_STATUS],
                                   '').format(**formatted_values)
        if descr:
            res.append('{}\'{}\' {}'.format('Property ', full_key, descr))
    return res


def get_new_prefix(prefix, key):
    if not prefix:
        return key
    return '{}.{}'.format(prefix, key)


def to_string(value):
    if isinstance(value, dict):
        res = '[complex value]'
    elif isinstance(value, str):
        res = '\'{}\''.format(value)
    elif value is True or value is False or value is None:
        res = {True: 'true', False: 'false', None: 'null'}[value]
    else:
        res = value
    return res
