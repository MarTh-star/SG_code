from connect import sql_execute

def create_table(table_name = 'sollfrequenz'):
    # build query
    query =   f'''
		CREATE TABLE {table_name} (
			Datum_Zeit timestamp without time zone,
			A_f_soll_aktiv_Hz int,
            UNIQUE (Datum_Zeit)
			)
               '''

    sql_execute(query)
    return True

