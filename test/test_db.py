import psycopg2
import unittest


class TestDatabase(unittest.TestCase): 

    def setUp(self): #creo la conexion a la base de datos

        self.conn = psycopg2.connect("postgresql://postgres:9697@localhost:5432/microservicio_order")
        self.cur = self.conn.cursor()
        
    def tearDown(self): #cierro la conexion a la base de datos

        self.cur.close()
        self.conn.close()

    def test_connection(self): #test de conexion a la base de datos
        self.assertIsNotNone(self.conn)

  
    
if __name__ == '__main__':
    unittest.main()

