import os
import json
from kafka import KafkaProducer
from apps.common.serializer import Serializers
serializers = Serializers()


class Kf:
    def __init__(self):
        self.producer = KafkaProducer(
            value_serializer=lambda v: serializers.json_serialize(v),
            key_serializer=lambda k: serializers.json_serialize(k),
            bootstrap_servers=os.environ.get("BOOTSTRAP_SERVER"),
            sasl_plain_username=os.environ.get("AV_KFUSER"),
            sasl_plain_password=os.environ.get("AV_KFPASSWORD"),
            security_protocol="SASL_SSL",
            ssl_cafile="apps/common/cq.pem",
            sasl_mechanism="PLAIN",
        )

    def send_data(self, key, data):
        self.producer.send('site-monitor', key=key, value=data)
        self.producer.flush()