import json


def is_json(input_json):
    try:
        json.loads(input_json)
    except ValueError:
        return False
    return True
