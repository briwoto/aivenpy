run_aiven:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python aiven/aiven.py

start_consumer:
	PYTHONPATH="apps:db:aiven:$(PYTHONPATH)" python -c 'from aiven import aiven; aiven.start_consumer()'

run_tests:
	python -m pytest tests/