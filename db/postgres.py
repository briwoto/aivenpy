import psycopg2
import os
from aiven import config
log = config.get_logger()


class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=os.environ.get("DB_HOST"),
                    port=os.environ.get("DB_PORT"),
                    database=os.environ.get("DATABASE"),
                    user=os.environ.get("DB_USER"),
                    password=os.environ.get("DB_PASSWORD")
                )
                self.cur = self.conn.cursor()
                self.cur.execute('SELECT version()')
                log.info(self.cur.fetchone())
            except Exception as e:
                log.error(f'EXCEPTION OCCURED when connecting to db\n{str(e)}')
                return None, None

    def close_connection(self):
        if self.cur:
            self.cur.close()
            self.conn.close()

    def run_sql(self, sql_str, val=None):
        self.cur.execute(sql_str, val)
        self.conn.commit()

    def get_data_list(self, sql_str):
        self.cur.execute(sql_str)
        return self.cur
