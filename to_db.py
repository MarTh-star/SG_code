import re
from connect import sql_execute

def remove_substring_from_start(long_string):
    pattern = r'^[A-Z][a-z]\. '  #To remove the beginning part to easier transform into timestamp
    result = re.sub(pattern, '', long_string)
    return result

#Inserts rows of a dataframe into table
def insert_data_into_database(df_data, table_name):
    for row in df_data.itertuples():
        date = remove_substring_from_start(row.Datum_Zeit)
        # print(row)
        query = f'''
                INSERT INTO {table_name} (A_f_soll_aktiv_Hz, Datum_Zeit)
                VALUES ({row.A_f_soll_aktiv_Hz}, TO_TIMESTAMP('{date}', 'DD.MM.YY')::timestamp without time zone)
                ON CONFLICT (Datum_Zeit) DO NOTHING
                '''

        # print(query)
        sql_execute(query)

    return True

#To insert original test data
#insert_data_into_database(df, 'sollfrequenz')
