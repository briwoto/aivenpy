import os
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
            sasl_plain_username=os.environ.get("AV_KFUSER"),
            sasl_plain_password=os.environ.get("AV_KFPASSWORD"),
            security_protocol="SASL_SSL",
            ssl_cafile="apps/common/cq.pem",
            sasl_mechanism="PLAIN",
        )

    def send_data(self, topic, key, data):
        if not self.producer:
            self.connect()
        res = self.producer.send(topic, key=key, value=data)
        self.producer.flush()
        return res
