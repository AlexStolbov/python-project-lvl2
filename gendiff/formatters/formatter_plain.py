from gendiff.logout import log_info
import gendiff.make_inner_diff as inner_diff

DESCR_TEMPLATE = {
    inner_diff.STATUS_CHANGE: 'was updated. From {_DEL_} to {_NEW_}',
    inner_diff.STATUS_DEL: 'was removed',
    inner_diff.STATUS_NEW: 'was added with value: {_NEW_}'}


def get_plain(diff):
    plain = diff_to_list(diff, '')
    res = '\n'.join(plain)
    log_info('plain diff', res)
    return res


def diff_to_list(diff, prefix=''):
    res = []
    new_prefix = get_new_prefix(prefix, diff[inner_diff.KEY_KEY])
    if inner_diff.KEY_CHILDREN not in diff:
        values_to_string = {k: to_string(v) for k, v in
                            diff[inner_diff.KEY_VALUE].items()}

        descr = DESCR_TEMPLATE.get(diff[inner_diff.KEY_STATUS],
                                   '').format(**values_to_string)
        return ['{}\'{}\' {}'.format('Property ', new_prefix, descr)]

    children = filter(lambda key_descr: inner_diff.STATUS_STAY != key_descr.get(
        inner_diff.KEY_STATUS, None), diff[inner_diff.KEY_CHILDREN])
    for child in children:
        res += diff_to_list(child, new_prefix)
    res.sort()
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
