import requests
import re
import datetime
import logging
from db import talker


class SiteMonitor:
    def __init__(self):
        self.site_id = None
        self.base_url = None
        self.target_regex = None

    def get_stats(self):
        try:
            ar_data = []
            cur = talker.get_sites()
            row = cur.fetchone()
            while row is not None:
                self.site_id = row[0]
                self.base_url = row[1]
                self.target_regex = row[2]
                try:
                    val = self.set_data(res=requests.get(self.base_url, timeout=5))
                except Exception as e:
                    val = self.set_data(ex=str(e))
                data = {
                    "key": {"site_id": self.site_id},
                    "value": val
                }
                ar_data.append(data)
                row = cur.fetchone()
            return ar_data
        except Exception as e:
            logging.error(f'Get stats Exception Occured\n{str(e)}')
            return None

    def set_data(self, res=None, ex=None):
        if res is not None:
            has_button = False if not re.search(self.target_regex, res.text) else True
            return {
                "site_id": self.site_id,
                "status_code": res.status_code,
                "response_time": res.elapsed.total_seconds(),
                "has_regexp": has_button,
                "created": str(datetime.datetime.now()),
                "modified": str(datetime.datetime.now()),
                "comments": ""
            }
        str_ex = str(ex) if ex is not None else ""
        return {
            "site_id": self.site_id,
            "status_code": None,
            "response_time": None,
            "has_regexp": None,
            "created": str(datetime.datetime.now()),
            "modified": str(datetime.datetime.now()),
            "comments": f'Request Exception: {str_ex}'
        }
