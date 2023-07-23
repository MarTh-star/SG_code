import psycopg2
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

def db_connect():
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('dbConfig.ini')

    con = psycopg2.connect(
        host = config.get('postgresql', 'host'),
        database = config.get('postgresql', 'database'),
        user = config.get('postgresql', 'user'),
        password = config.get('postgresql', 'password')
        )
    
    return con

def sql_execute_and_fetch(query):
    con = db_connect()
    #create cursor to use
    cursor = con.cursor()
    # Execute query with provided parameters
    cursor.execute(query)
    #Save result before closing
    result = cursor.fetchall()
    #close cursor
    cursor.close()
    #close connection
    con.close()
    return result

def sql_execute(query):
    con = db_connect()
    #create cursor to use
    cursor = con.cursor()
    # Execute query with provided parameters
    cursor.execute(query)
    con.commit()
    #close cursor
    cursor.close()
    #close connection
    con.close()
    return True