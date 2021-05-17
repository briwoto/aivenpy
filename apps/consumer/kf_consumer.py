import os
from kafka import KafkaConsumer
from apps.common import serializer


def get_consumer():
    return KafkaConsumer(
        'site-monitor',
        bootstrap_servers=os.environ.get("BOOTSTRAP_SERVER"),
        sasl_plain_username=os.environ.get("KF_USER"),
        sasl_plain_password=os.environ.get("KF_PASSWORD"),
        security_protocol="SASL_SSL",
        ssl_cafile="apps/common/ca.pem",
        sasl_mechanism="PLAIN",
        group_id='monitor-group',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: serializer.json_deserialize(v),
        key_deserializer=lambda k: serializer.json_deserialize(k),
    )
