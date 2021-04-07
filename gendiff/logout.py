import logging
import pprint


def log_info(message, data):
    if isinstance(data, dict) or isinstance(data, list):
        data_to_log = pprint.pformat(data, indent=2, compact=True,
                                     sort_dicts=False)
    else:
        data_to_log = data
    logging.info('{}: \n{}'.format(message, data_to_log))
