from kafka import KafkaConsumer
import os
from apps.common.serializer import Serializers
import consumer_queries
serializer = Serializers()


def consume_data():
    consumer = KafkaConsumer(
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
    for message in consumer:
        consumer_queries.add_site_monitor_data_to_db((message.key, message.value))


if __name__ == "__main__":
    consume_data()
