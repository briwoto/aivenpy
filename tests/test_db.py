import logging
from db.postgres import Postgres
postgres = Postgres()


def test_db_is_accessible():
    con, cur = postgres.connect()
    postgres.close_connection()
    assert True if con is not None and cur is not None else False


def test_no_exception_raised_when_querying_database():
    con, cur = postgres.connect()
    try:
        cur.execute("SELECT * FROM site_monitor")
        postgres.close_connection()
        assert True
    except Exception as e:
        logging.info(f'UnitTest test_querying_to_database EXCEPTION OCCURED\n{str(e)}')
        assert False
