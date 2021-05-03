import json


def json_serialize(data):
    return json.dumps(data).encode('utf-8')


def json_deserialize(data):
    return json.loads(data.decode('utf-8'))
