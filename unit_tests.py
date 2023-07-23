import unittest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import pandas as pd
import psycopg2
import to_db
import api_queries
import create_table
from connect import db_connect

class TestInsertData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Create test data
        data = pd.DataFrame({
            'Datum_Zeit': ['2023-07-01 12:00:00', '2023-07-01 13:00:00'],
            'A_f_soll_aktiv_Hz': [50.0, 51.0]
        })
        to_db.insert_data_into_database(data, 'test_table3')

    def test_data_inserted_correctly(self):
        # Connect test database
        con = db_connect()
        cursor = con.cursor()

        #Check that it was entered correctly
        cursor.execute('SELECT COUNT(*) FROM test_table3')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 4)

        # Clean up
        cursor.close()
        con.close()

class TestCreateSollfrequenzTable(unittest.TestCase):

    @patch('create_table.psycopg2.connect')
    def test_create_table(self, mock_connect):
        mock_connection = mock_connect.return_value
        mock_cursor = mock_connection.cursor.return_value

        create_table.create_table('test_table8')

        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()



class TestFastAPI(unittest.TestCase):
    def setUp(self):
 
        self.client = TestClient(api_queries.app)

    def test_execute_query(self):
     
        response = self.client.get(
            "/data",
            params={
                "start_time": "2023-07-01 00:00:00",
                "end_time": "2023-07-02 00:00:00",
                "interval_minutes": 60,
                "limit": 5
            }
        )
        self.assertEqual(response.status_code, 200) 
    

    def test_execute_query_invalid_parameters(self):
    
        response = self.client.get("/data")
        self.assertEqual(response.status_code, 422)  

        response = self.client.get(
            "/data",
            params={
                "start_time": "2023-07-01 00:00:00",
                "end_time": "2023-07-02 00:00:00",
                "interval_minutes": "invalid",
                "limit": 5
            }
        )
        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    unittest.main()