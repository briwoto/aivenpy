import datetime
from db import talker
from aiven import config
log = config.get_logger()


def add_site_monitor_data_to_db(data):
    print(data[1])
    key = data[0]
    val = data[1]
    query_data = {
        "site_id": key["site_id"],
        "status_code": val["status_code"],
        "response_time": val["response_time"],
        "record_date": val["modified"],
        "has_regexp": val["has_regexp"],
        "comments": val["comments"],
        "inserted_date": datetime.datetime.now()
    }
    column_names = ','.join(query_data.keys())
    ar_values = list(map(lambda x: x if len(str(x)) else None, query_data.values()))
    talker.insert_data('site_monitor', column_names, ar_values)
    log.info('Data inserted')
