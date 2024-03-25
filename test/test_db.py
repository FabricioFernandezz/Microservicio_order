import unittest 
from flask import current_app
from sqlalchemy import text
from app.models.order import Order

from app import create_app, db


class AppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_db_connection(self):
        result = db.session.query(text("hello word"))
        self.assertEqual(result[0], "hello word")
    
    def test_app(self):
        self.assertTrue(self.app.testing)
        self.assertTrue(current_app.config['TESTING'])
        
    def test_order(self):
        order = Order(id_order=1, id_client='client_id', id_product='product_id', payment_method='cash', total='100')

        # Verifica los atributos de la orden
        self.assertEqual(order.id_order, 1)
        self.assertEqual(order.id_client, 'client_id')
        self.assertEqual(order.id_product, 'product_id')
        self.assertEqual(order.payment_method, 'cash')
        self.assertEqual(order.total, '100')