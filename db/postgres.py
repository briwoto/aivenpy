import psycopg2
import os
import logging


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
            logging.info("connected to db")
            self.cur.execute('SELECT version()')
            logging.info(self.cur.fetchone())
            return self.conn, self.cur
        except Exception as e:
            logging.error(f'EXCEPTION OCCURED when connecting to db\n{str(e)}')
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
        logging.info('Data inserted')
