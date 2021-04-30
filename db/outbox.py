class Outbox:
    def __init__(self):
        self.columns = """topic,item_key,item_value,created,modified,published,comments"""

    @staticmethod
    def get_insert_sql(rawdata):
        try:
            query = """
                INSERT INTO outbox (topic,item_key,item_value,created,modified,published,comments)
                VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                rawdata["topic"],
                rawdata["item_key"],
                rawdata["item_value"],
                rawdata["created"],
                rawdata["modified"],
                rawdata["published"],
                rawdata["comments"]
            )
            return query, data
        except Exception as e:
            print(str(e))
            return None
