import os
import atexit
from kafka import KafkaConsumer
from aiven import config
from apps.common import serializer
import consumer_queries
config.create_pem_file()


def consume_data():
    consumer = get_consumer()
    for message in consumer:
        consumer_queries.add_site_monitor_data_to_db((message.key, message.value))


def get_consumer():
    return KafkaConsumer(
        'site-monitor',
        bootstrap_servers=os.environ.get("BOOTSTRAP_SERVER"),
        sasl_plain_username=os.environ.get("AV_KFUSER"),
        sasl_plain_password=os.environ.get("AV_KFPASSWORD"),
        security_protocol="SASL_SSL",
        ssl_cafile="apps/common/cq.pem",
        sasl_mechanism="PLAIN",
        group_id='monitor-group',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: serializer.json_deserialize(v),
        key_deserializer=lambda k: serializer.json_deserialize(k),
    )


if __name__ == "__main__":
    atexit.register(config.delete_pem_at_exit)
    consume_data()
