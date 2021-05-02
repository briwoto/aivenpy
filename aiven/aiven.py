from apps.site_monitor.monitor import SiteMonitor
from apps.producer.kafka_producer import Kf
import config
import atexit
config.create_pem_file()
mon = SiteMonitor()
kf = Kf()


def aiven():
    stats = mon.get_stats()
    if not stats:
        print('stats not received. exiting program')
        quit()
    kf.send_data('site-monitor', {"site_id": 1}, stats)
    print("Data sent")


if __name__ == '__main__':
    atexit.register(config.delete_pem_at_exit)
    aiven()
