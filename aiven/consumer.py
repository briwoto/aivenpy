from apps.consumer import consumer_queries
from apps.consumer import kf_consumer
import config
import atexit
config.create_pem_file()


def start_consumer():
    msg_object = kf_consumer.get_consumer()
    if isinstance(msg_object, Exception):
        log.error(f'Kafka Consumer CONNECTION EXCEPTION:\n{type(msg_object).__name__}: {str(msg_object)}')
        quit()
    try:
        for message in msg_object:
            consumer_queries.add_site_monitor_data_to_db((message.key, message.value))
    except Exception as e:
        log.error(f'Kafka messages EXCEPTION OCCURED:\n{str(e)}')


if __name__ == '__main__':
    log = config.get_logger()
    atexit.register(config.delete_pem_at_exit)
    start_consumer()
