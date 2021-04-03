import json
import yaml

JSON_FORMAT = 'json'
YAML_FORMAT = 'yaml'


def parse(data, data_format):
    if data_format == JSON_FORMAT:
        return json.load(data)
    elif data_format == YAML_FORMAT:
        return yaml.safe_load(data)
    else:
        return None
