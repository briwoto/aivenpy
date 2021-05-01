run_aiven:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python aiven/aiven.py

start_consumer:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python apps/consumer/kafka_consumer.py

run_tests:
	python -m pytest