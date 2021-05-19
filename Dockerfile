FROM python:3.8.9-alpine3.12

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install psycopg2-binary

RUN pip3 install -r requirements.txt

ENV PYTHONPATH="apps:db:aiven:${PYTHONPATH}"
ENV DATABASE=${DATABASE}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV KF_USER=${KF_USER}
ENV KF_PASSWORD=${KF_PASSWORD}
ENV KF_PORT=${KF_PORT}
ENV BOOTSTRAP_SERVER=${BOOTSTRAP_SERVER}
ENV CA_PEM=${CA_PEM}

COPY . .

CMD [ "python3", "aiven/consumer.py"]