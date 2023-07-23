from fastapi import FastAPI
import to_db
import create_table
from connect import sql_execute, sql_execute_and_fetch
from csv_to_df import prepare_dataframe

app = FastAPI()

#FastAPI to query 
@app.get("/data")
def get_data(start_time, end_time, interval_minutes: int, table_name = 'sollfrequenz'):

    # Convert interval_minutes to seconds
    interval_seconds = int(interval_minutes) * 60

    #Build query
    query = f'''
            SELECT *
            FROM {table_name}
            WHERE datum_zeit BETWEEN '{start_time}'::timestamp without time zone
            AND '{end_time}'::timestamp without time zone
            AND EXTRACT(EPOCH FROM datum_zeit) % {interval_seconds} = 0;
            '''
   
    return sql_execute_and_fetch(query)

@app.post("/input_test_data")
def input_test_data(table_name = 'sollfrequenz'):
    to_db.insert_data_into_database(prepare_dataframe(), table_name)

@app.post("/create_table")
def create_new_table(table_name = 'sollfrequenz'):
    create_table.create_table(table_name)

@app.get("/get_top")
def get_top(table_name = 'sollfrequenz', number=10):
    
    #Build query
    query = f'''
            SELECT *
            FROM {table_name}
            LIMIT {number};
            '''
    
    return sql_execute_and_fetch(query)