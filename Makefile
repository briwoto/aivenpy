monitor_producer:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python aiven/monitor_producer.py

consumer:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python aiven/consumer.py

run_tests:
	python -m pytest tests/