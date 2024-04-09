import unittest
from app import create_app, db
from sqlalchemy import text
from app.models import Order

class DatabaseTestCase(unittest.TestCase):

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
        result= db.session.query(text("'probando'")).one()
        self.assertEqual(result[0], 'probando')
    
    def test_create_order(self):
        order = Order(id_order=1,id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        db.session.add(order)
        db.session.commit()
        self.assertIsNotNone(order.id_order)

    def test_update_order(self):
        order = Order(id_order=1,id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        db.session.add(order)
        db.session.commit()
        order.total = '200'
        db.session.commit()
        self.assertEqual(order.total, '200')

    def test_delete_order(self):
        order = Order(id_order=1,id_client='client_id', id_product='product_id', payment_method='cash', total='100')
        db.session.add(order)
        db.session.commit()
        db.session.delete(order)
        db.session.commit()
        self.assertIsNone(Order.query.get(1))


if __name__ == '__main__':
    unittest.main()