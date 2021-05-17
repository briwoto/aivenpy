from db.postgres import Postgres

postgres = Postgres()


def insert_data(tablename, column_names: str, ar_values: list):
    insert_clause = f'INSERT INTO {tablename} ({column_names})'
    values_clause = f'values ({",".join(["%s"] * len(ar_values))})'
    postgres.run_sql(f'{insert_clause} \n{values_clause}', tuple(ar_values))


def get_sites(table_name='sites', get_columns='id, url, regexp'):
    select_clause = f'select {get_columns} from {table_name}'
    return postgres.get_data_list(select_clause)
