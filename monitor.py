import requests
import re
import os
from db.postgres import Postgres
postgres = Postgres()
base_url = os.environ.get("AVBASE_URL")


def monitor():
    postgres.connect()
    btn = "<button.*>?STAY UPDATED</button>"
    try:
        res = requests.get(base_url, timeout=5)
        has_button = False if not re.search(btn, res.text) else True
        stats: dict = {
            "status_code": res.status_code,
            "response_time": res.elapsed.total_seconds(),
            "has_button": has_button
        }
        print(stats)
    except Exception as e:
        print("Unable to Connect to base url. Exception Occured")
        print(str(e))


monitor()
