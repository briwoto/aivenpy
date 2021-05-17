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
        quit()
    return stats


def run_producer(data):
    for row in data:
        producer.send_data('site-monitor', row["key"], row["value"])
        log.info("Data sent")


if __name__ == '__main__':
    atexit.register(config.delete_pem_at_exit)
    sites_data = run_monitor()
    try:
        run_producer(sites_data)
    except Exception as e:
        log.error(f'Run kafka producer EXCEPTION OCCURED:\n{str(e)}')
