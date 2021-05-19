import os
import time

from kafka import KafkaProducer
from apps.common import serializer


class Kf:
    def __init__(self):
        self.producer = None

    def connect(self):
        self.producer = KafkaProducer(
            value_serializer=lambda v: serializer.json_serialize(v),
            key_serializer=lambda k: serializer.json_serialize(k),
            bootstrap_servers=os.environ.get("BOOTSTRAP_SERVER"),
            sasl_plain_username=os.environ.get("KF_USER"),
            sasl_plain_password=os.environ.get("KF_PASSWORD"),
            security_protocol="SASL_SSL",
            ssl_cafile="apps/common/ca.pem",
            sasl_mechanism="PLAIN",
            connections_max_idle_ms=5000,
        )

    def send_data(self, topic, key, data):
        try:
            if not self.producer:
                self.connect()
            res = self.producer.send(topic, key=key, value=data)
            self.producer.flush()
            time.sleep(1)
            return res
        except Exception as e:
            return e

    def close_producer(self):
        self.producer.close()
