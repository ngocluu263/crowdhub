import json


def is_json(input_json):
    try:
        json.loads(input_json)
    except ValueError:
        return False
    return True


def load_json(input_json):
    if isinstance(input_json, dict):
        return input_json
    return json.loads(input_json)
