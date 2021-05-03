import psycopg2
import os
from aiven import config
log = config.get_logger()


class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=os.environ.get("AVHOST"),
                port=os.environ.get("AVPORT"),
                database=os.environ.get("AVDATABASE"),
                user=os.environ.get("AVUSER"),
                password=os.environ.get("AVPASSWORD")
            )
            self.cur = self.conn.cursor()
            self.cur.execute('SELECT version()')
            log.info(self.cur.fetchone())
            return self.conn, self.cur
        except Exception as e:
            log.error(f'EXCEPTION OCCURED when connecting to db\n{str(e)}')
            return None, None

    def close_connection(self):
        if self.cur:
            self.cur.close()
            self.conn.close()

    def run_sql(self, sql_str, val=None):
        con, cur = self.connect()
        cur.execute(sql_str, val)
        con.commit()
        self.close_connection()
