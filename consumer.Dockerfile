FROM python:3.8.9-alpine3.12

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install psycopg2-binary

RUN pip3 install -r requirements.txt

ENV PYTHONPATH="apps:db:aiven:${PYTHONPATH}"
ENV PYTHONUNBUFFERED=1
ENV AVDATABASE=""
ENV AVHOST=""
ENV AVPORT=""
ENV AVUSER=""
ENV AVPASSWORD=""
ENV AV_BASE_URL=""
ENV AV_KFUSER=""
ENV AV_KFPASSWORD=""
ENV AV_KFPORT=""
ENV BOOTSTRAP_SERVER=""

COPY . .

CMD [ "python3", "apps/consumer/kafka_consumer.py"]