import json
import yaml


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)
