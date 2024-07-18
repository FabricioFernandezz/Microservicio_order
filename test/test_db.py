import unittest
import psycopg2
import os
from dotenv import load_dotenv


class DatabaseTestCase(unittest.TestCase):


    def setUp(self):
        load_dotenv()
        self.connection = psycopg2.connect(
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DB"),
            port=os.getenv("PORT_DB")
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()
    
    def test_db_connection(self):
        print("Testing database connection")
        self.assertIsNotNone(self.connection)

if __name__ == "__main__":
    unittest.main()