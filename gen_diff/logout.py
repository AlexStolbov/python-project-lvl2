import logging
import pprint


def log_info(message, data):
    if isinstance(data, dict):
        data_to_log = pprint.pformat(data, indent=2, compact=True)
    else:
        data_to_log = data
    logging.info('{}: \n{}'.format(message, data_to_log))
