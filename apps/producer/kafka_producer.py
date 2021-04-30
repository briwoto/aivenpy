from kafka import KafkaProducer
import json
import os


class Kf:
    def __init__(self):
        self.producer = KafkaProducer(
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda v: json.dumps(v).encode('utf-8'),
            bootstrap_servers=['localhost:9092'],
        )

    def send_data(self, key, data):
        self.producer.send('site-monitor', key=key, value=data)
        self.producer.flush()


