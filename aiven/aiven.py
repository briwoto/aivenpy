from apps.producer.kafka_producer import Kf
from apps.consumer import consumer_queries
from apps.consumer import kf_consumer
from apps.site_monitor.monitor import SiteMonitor
import config
import atexit
log = config.get_logger()
config.create_pem_file()
mon = SiteMonitor()
producer = Kf()


def aiven():
    stats = mon.get_stats()
    if not stats:
        log.error('stats not received. exiting program')
        quit()
    for row in stats:
        producer.send_data('site-monitor', row["key"], row["value"])
        log.info("Data sent")


def start_consumer():
    msg_object = kf_consumer.get_consumer()
    for message in msg_object:
        consumer_queries.add_site_monitor_data_to_db((message.key, message.value))


if __name__ == '__main__':
    atexit.register(config.delete_pem_at_exit)
    aiven()
