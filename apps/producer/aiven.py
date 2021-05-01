from apps.producer.monitor import SiteMonitor
from apps.producer.kafka_producer import Kf
mon = SiteMonitor()
kf = Kf()


def aiven():
    stats = mon.get_stats()
    if not stats:
        print('stats not received. exiting program')
        quit()
    kf.send_data({"site_id": 1}, stats)
    print("Data sent")


aiven()