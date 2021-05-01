from db.postgres import Postgres

postgres = Postgres()


def insert_data(tablename, data, data_format="json"):
    column_names = ','.join(data.keys())
    ar_values = list(map(lambda x: x if len(str(x)) else None, data.values()))
    ar = ["%s"] * len(ar_values)
    str_ar = ','.join(ar)
    insert_clause = f'INSERT INTO {tablename} ({column_names})'
    values_clause = f'values ({str_ar})'
    postgres.run_sql(f'{insert_clause} \n{values_clause}', tuple(ar_values))
