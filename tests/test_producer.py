import atexit
import os
from apps.producer.kafka_producer import Kf
from aiven import config
config.create_pem_file()
kf = Kf()


def test_producer_is_working():
    atexit.register(config.delete_pem_at_exit)
    data = {
        "type": "testing",
        "area": "kafka producer"
    }
    kf.connect()
    res = kf.send_data('tests', {'user': 'Rahul'}, data)
    assert res.exception is None
