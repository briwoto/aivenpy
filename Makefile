run_producer:
	PYTHONPATH="apps:$(PYTHONPATH)" python apps/producer/aiven.py

start_consumer:
	PYTHONPATH="apps:$(PYTHONPATH)" python apps/consumer/kafka_consumer.py
