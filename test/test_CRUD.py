# from app import create_app, db
# from app.models import Order, Client, Product
# from app.services import OrderService
# import unittest
# from flask_caching import Cache

# class TestCRUD(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.order_service = OrderService()

#     def setUp(self):
#         self.app = create_app() 
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()

#     def test_create(self):
#         # Crear instancias de Client y Product
#         client = Client(name='Test Client', surname='test', phone_number='260525255', email='test@client.com', dni='123456', address='test', password='test')
#         product = Product(name='Test Product', price='100', brand='test', size='test', stock='100')

#         # Guardar las instancias en la base de datos
#         db.session.add(client)
#         db.session.add(product)
#         db.session.commit()

#         # Crear una orden con los IDs de las instancias creadas
#         order = Order(id_client=client.id, id_product=product.id, payment_method='cash', total='100')
#         created_order = self.order_service.create(order)

#         # Realizar las aserciones
#         self.assertEqual(created_order.id_client, client.id)
#         self.assertEqual(created_order.id_product, product.id)
#         self.assertEqual(created_order.payment_method, 'cash')
#         self.assertEqual(created_order.total, '100')

#     def test_find_by_id(self):
#         # Crear instancias de Client y Product
#         client = Client(name='Test Client', email='test@client.com')
#         product = Product(name='Test Product', price=100)

#         # Guardar las instancias en la base de datos
#         db.session.add(client)
#         db.session.add(product)
#         db.session.commit()

#         # Crear una orden con los IDs de las instancias creadas
#         order = Order(id_client=client.id, id_product=product.id, payment_method='cash', total='100')
#         db.session.add(order)
#         db.session.commit()

#         # Buscar la orden por ID
#         found_order = self.order_service.find_by_id(order.id)

#         # Realizar las aserciones
#         self.assertEqual(found_order.id, order.id)

#         def test_find_all(self):
#             order = Order(id_client='client_id', id_product='product_id', payment_method='cash', total='100')
#             self.order_service.create(order)
#             orders = self.order_service.find_all()
#             self.assertEqual(len(orders), 1)
#             self.assertEqual(orders[0].id_client, 'client_id')
#             self.assertEqual(orders[0].id_product, 'product_id')
#             self.assertEqual(orders[0].payment_method, 'cash')
#             self.assertEqual(orders[0].total, '100')

#         def test_update(self):
#             order = Order( id_client='client_id', id_product='product_id', payment_method='cash', total='100')
#             self.order_service.create(order)
#             updated_order = self.order_service.update(Order(id_client='client_id', id_product='product_id', payment_method='credit', total='100'), 1)
#             self.assertEqual(updated_order.payment_method, 'credit')
            
#         def test_delete(self):
#             order = Order( id_client='client_id', id_product='product_id', payment_method='cash', total='100')
#             created_order = self.order_service.create(order)
#             self.order_service.delete(created_order.id_order)
#             self.assertIsNone(self.order_service.find_by_id(created_order.id_order))
            
# if __name__ == '__main__':
#     unittest.main()
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app, db
from app.models import Client, Product, Order
from app.services import OrderService


class OrderTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.order_service = OrderService()

    def setUp(self):
        super(OrderTestCase, self).setUp()
        self.app = create_app() 
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.order_service = self.__class__.order_service

    def tearDown(self):
        db.session.rollback()
        self.app_context.pop()

    def create_client(self):
        client = Client(
            name='Client 1',
            surname='Client 1 Surname',
            phone_number='123456789',
            email='clientemail@gmail.com',
            dni='123456786',
            address='Client 1 Address',
            password='clientpassword'
        )
        db.session.add(client)
        db.session.commit()
        return client

    def create_product(self):
        product = Product(
            name='Test Product',
            price=100,
            brand='Test Brand',
            size='Test Size',
            stock=100
        )
        db.session.add(product)
        db.session.commit()
        return product

    def create_order(self, id_client, id_product, payment_method='cash', total='100'):
        order = Order(
            id_client=id_client,
            id_product=id_product,
            payment_method=payment_method,
            total=total
    )
        db.session.add(order)
        db.session.commit()
        return order

    def test_create_client(self):
        client = self.create_client()
        print(f'Client ID: {client.id}')
        self.assertIsNotNone(client.id)
        # self.assertTrue(client.id)

    def test_create_product(self):
        product = self.create_product()
        print(f'Product ID: {product.id}')
        self.assertTrue(product.id)

    def test_create_order(self):
        client = self.create_client()
        product = self.create_product()
        order = self.create_order(client.id, product.id, 'prueba', '100')
        self.order_service.create(order)
        print(f'Order ID: {order.id_order}')
        self.assertIsNotNone(order.id_order)
        # self.assertTrue(order.id_order)
        # self.assertEqual(order.id_client, client.id)
        # self.assertEqual(order.id_product, product.id)
    
    def test_find_by_id(self):
        client = self.create_client()
        product = self.create_product()
        order = self.create_order(client.id, product.id, 'cash', '100')
        found_order = self.order_service.find_by_id(order.id_order)
        self.assertEqual(found_order.id_order, order.id_order)

    def test_update(self):
        client = self.create_client()
        product = self.create_product()
        order = self.create_order(client.id, product.id, 'cash', '100')
        updated_order = self.order_service.update(Order(id_client=client.id, id_product=product.id, payment_method='credit', total='100'), order.id_order)
        self.assertEqual(updated_order.payment_method, 'credit')
    
    def test_delete(self):
        client = self.create_client()
        product = self.create_product()
        order = self.create_order(client.id, product.id, 'cash', '100')
        self.order_service.delete(order.id_order)
        self.assertIsNone(self.order_service.find_by_id(order.id_order))


if __name__ == '__main__':
    unittest.main()
