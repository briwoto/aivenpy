import json


class Serializers:
    def json_serializer(self, data):
        return json.dumps(data).encode('utf-8')
