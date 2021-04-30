import requests
import re
import os
base_url = os.environ.get("BASE_URL")


def monitor():
    # from db.postgres import connect
    # connect()
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
        print(str(e))


monitor()
