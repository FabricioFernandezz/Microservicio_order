from app.models.order import Order
from marshmallow import Schema,validate, fields, Schema, post_load

class OrderSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id_order = fields.Integer(attribute='id_order', data_key='id_order')
    id_client = fields.String(attribute='id_client', data_key='id_client')
    id_product = fields.String(attribute='id_product', data_key='id_product')
    payment_method = fields.String(attribute='payment_method', data_key='payment_method')
    total = fields.String(attribute='total', data_key='total')

    @post_load
    def make_order(self, data, **kwargs):
        return Order(**data)