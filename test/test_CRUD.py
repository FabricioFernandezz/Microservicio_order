from app import create_app, db
from app.models import Order
from app.services import OrderService
import unittest

class TestCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.order_service = OrderService()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        created_order = self.order_service.create(order)
        self.assertEqual(created_order.id_order, 1)
        self.assertEqual(created_order.id_client, 'client_id')
        self.assertEqual(created_order.id_product, 'product_id')
        self.assertEqual(created_order.payment_method, 'cash')
        self.assertEqual(created_order.total, '100')


    def test_find_by_id(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        self.order_service.create(order)
        found_order = self.order_service.find_by_id(1)
        self.assertEqual(found_order.id_order, 1)
        self.assertEqual(found_order.id_client, 'client_id')
        self.assertEqual(found_order.id_product, 'product_id')
        self.assertEqual(found_order.payment_method, 'cash')
        self.assertEqual(found_order.total, '100')


    def test_find_all(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        self.order_service.create(order)
        orders = self.order_service.find_all()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].id_order, 1)
        self.assertEqual(orders[0].id_client, 'client_id')
        self.assertEqual(orders[0].id_product, 'product_id')
        self.assertEqual(orders[0].payment_method, 'cash')
        self.assertEqual(orders[0].total, '100')

    def test_update(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        self.order_service.create(order)
        updated_order = self.order_service.update(Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='credit', total='100'), 1)
        self.assertEqual(updated_order.payment_method, 'credit')
        
    def test_delete(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        created_order = self.order_service.create(order)
        self.order_service.delete(created_order.id_order)
        self.assertIsNone(self.order_service.find_by_id(1))
        
if __name__ == '__main__':
    unittest.main()
