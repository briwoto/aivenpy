import psycopg2
import os
from .outbox import Outbox
outbox = Outbox()


class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=os.environ.get("AVHOST"),
            port=os.environ.get("AVPORT"),
            database=os.environ.get("AVDATABASE"),
            user=os.environ.get("AVUSER"),
            password=os.environ.get("AVPASSWORD")
        )
        self.cur = self.conn.cursor()
        print("connected to db")
        self.cur.execute('SELECT version()')
        print(self.cur.fetchone())
        return self.cur

    def close_connection(self):
        print('cursor is')
        if self.cur:
            self.cur.close()
            self.conn.close()

    def insert_data_in_outbox(self, rawdata):
        print(outbox.get_insert_sql(rawdata))
