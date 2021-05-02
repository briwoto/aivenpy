from apps.producer.kafka_producer import Kf

kf = Kf()


def test_producer_is_working():
    data = {
        "type": "testing",
        "area": "kafka producer"
    }
    res = kf.send_data('tests', {'user': 'Rahul'}, data)
    assert res.exception is None
