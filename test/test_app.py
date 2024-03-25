
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
      
    def test_order(self):
        # Crea una instancia de la clase Order con valores adecuados
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')

        # Verifica los atributos de la orden
        self.assertEqual(order.id_order, 1)
        self.assertEqual(order.id_client, 'client_id')
        self.assertEqual(order.id_product, 'product_id')
        self.assertEqual(order.payment_method, 'cash')
        self.assertEqual(order.total, '100')

    def test_app(self):
         self.app.config['TESTING'] = True
         self.assertTrue(self.app.config['TESTING'])
        

if __name__ == '__main__':
    unittest.main()





