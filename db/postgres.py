import psycopg2
import os


class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(
            host=os.environ.get("HOST"),
            port=os.environ.get("PORT"),
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD")
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
