from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        'site-monitor',
        bootstrap_servers='localhost:9092',
        group_id='monitor_group',
        auto_offset_reset='earliest',
    )
    for message in consumer:
        print(json.loads(message.value))