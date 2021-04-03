import logging
from gendiff.logout import log_info
from gendiff.open_source import open_source
from gendiff.parse_source import parse
from gendiff.make_inner_diff import compare_data
from gendiff.formatters.make_format import make_format


def generate_diff(file_old, file_new, out_format='stylish'):
    data_old = source_to_data(file_old)
    data_new = source_to_data(file_new)

    diff = []
    if data_old is not None and data_new is not None:
        inner_diff = compare_data(data_old, data_new)
        log_info('inner_diff', inner_diff)
        diff = make_format(inner_diff, out_format)
    return diff


def source_to_data(source):
    data_source, format_source = open_source(source)
    data = parse(data_source, format_source)
    return data


logging.basicConfig(filename='gendiff.log',
                    level=logging.INFO,
                    filemode='w',
                    format='%(levelname)s:%(message)s')
