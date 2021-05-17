from apps.consumer import consumer_queries
from apps.consumer import kf_consumer
import config
import atexit
log = config.get_logger()
config.create_pem_file()


def start_consumer():
    try:
        msg_object = kf_consumer.get_consumer()
        for message in msg_object:
            consumer_queries.add_site_monitor_data_to_db((message.key, message.value))
    except Exception as e:
        log.error(f'Kafka consumer EXCEPTION OCCURED:\n{str(e)}')


if __name__ == '__main__':
    atexit.register(config.delete_pem_at_exit)
    start_consumer()
