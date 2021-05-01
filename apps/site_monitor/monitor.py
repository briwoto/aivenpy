import requests
import re
import os
import datetime


class SiteMonitor:
    def __init__(self):
        self.base_url = os.environ.get("AV_BASE_URL")
        self.target_regex = "<button.*>?STAY UPDATED</button>"

    def get_stats(self):
        try:
            res = requests.get(self.base_url, timeout=5)
            has_button = False if not re.search(self.target_regex, res.text) else True
            data = {
                "data": {
                    "site_id": 1,
                    "status_code": res.status_code,
                    "response_time": res.elapsed.total_seconds(),
                    "has_regexp": has_button,
                    "created": str(datetime.datetime.now()),
                    "modified": str(datetime.datetime.now()),
                    "comments": ""
                }
            }
            return data
            # return self.format_stats_for_outbox(data)
        except Exception as e:
            print("Unable to Connect to base_url. Exception Occured")
            print(str(e))
            return None
