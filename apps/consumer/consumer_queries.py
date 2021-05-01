from db import talker


def add_site_monitor_data_to_db(data):
    key = data[0]
    val = data[1]["data"]
    query_data = {
        "site_id": key["site_id"],
        "status_code": val["status_code"],
        "response_time": val["response_time"],
        "record_date": val["modified"],
        "has_regexp": val["has_regexp"],
        "comments": val["comments"]
    }
    talker.insert_data('site_monitor', query_data)
