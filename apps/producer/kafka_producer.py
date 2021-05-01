import os
import json
from kafka import KafkaProducer
from apps.common.serializer import Serializers
serializers = Serializers()


class Kf:
    def __init__(self):
        self.producer = KafkaProducer(
            value_serializer=lambda v: serializers.json_serializer(v),
            key_serializer=lambda v: serializers.json_serializer(v),
            bootstrap_servers=['localhost:9092'],
        )

    def send_data(self, key, data):
        self.producer.send('site-monitor', key=key, value=data)
        self.producer.flush()
