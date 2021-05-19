from apps.producer.kafka_producer import Kf
from apps.site_monitor.monitor import SiteMonitor
import config
import atexit
log = config.get_logger()
config.create_pem_file()
mon = SiteMonitor()
producer = Kf()


def run_monitor():
    stats = mon.get_stats()
    if not stats:
        log.error('stats not received. exiting program')
        raise ValueError
    return stats


def run_producer(data):
    for row in data:
        obj = producer.send_data('site-monitor', row["key"], row["value"])
        if isinstance(obj, Exception):
            log.error(f'Kafka Producer error while sending data:\n{type(obj).__name__}: {str(obj)}')
            break
        log.info("Data sent")


if __name__ == '__main__':
    config.start_db()
    atexit.register(config.delete_pem_at_exit)
    atexit.register(config.stop_db)
    sites_data = run_monitor()
    run_producer(sites_data)
    producer.close_producer()
    config.stop_db()
