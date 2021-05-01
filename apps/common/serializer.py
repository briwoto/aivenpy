import json


class Serializers:
    def json_serialize(self, data):
        return json.dumps(data).encode('utf-8')

    def json_deserialize(self, data):
        return json.loads(data.decode('utf-8'))
