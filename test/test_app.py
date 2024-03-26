
from app.models.order import Order
from app import create_app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()  # Llama a create_app() sin argumentos
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
      

    def test_app(self):
         self.app.config['TESTING'] = True
         self.assertTrue(self.app.config['TESTING'])
        

if __name__ == '__main__':
    unittest.main()





