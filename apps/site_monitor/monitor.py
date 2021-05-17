import requests
import re
import os
import datetime
import logging
from db import talker


class SiteMonitor:
    def __init__(self):
        pass

    def get_stats(self):
        try:
            ar_data = []
            cur = talker.get_sites()
            row = cur.fetchone()
            while row is not None:
                site_id = row[0]
                base_url = row[1]
                target_regex = row[2]
                res = requests.get(base_url, timeout=5)
                has_button = False if not re.search(target_regex, res.text) else True
                data = {
                    "key": {
                        "site_id": site_id
                    },
                    "value": {
                        "site_id": site_id,
                        "status_code": res.status_code,
                        "response_time": res.elapsed.total_seconds(),
                        "has_regexp": has_button,
                        "created": str(datetime.datetime.now()),
                        "modified": str(datetime.datetime.now()),
                        "comments": ""
                    }
                }
                ar_data.append(data)
                row = cur.fetchone()
            return ar_data
        except Exception as e:
            logging.error(f'Unable to Connect to base_url. Exception Occured\n{str(e)}')
            return None
