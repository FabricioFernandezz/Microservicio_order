from app.models.client import Client
from marshmallow import Schema,validate, fields, Schema, post_load

class ClientSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = fields.Integer(attribute='id', data_key='id')
    name = fields.String(attribute='name', data_key='name')
    surname = fields.String(attribute='surname', data_key='surname')
    phone_number = fields.String(attribute='phone_number', data_key='phone_number')
    email = fields.String(attribute='email', data_key='email')
    dni = fields.String(attribute='dni', data_key='dni')
    address = fields.String(attribute='address', data_key='address')
    password = fields.String(attribute='password', data_key='password')

    @post_load
    def make_client(self, data, **kwargs):
        return Client(**data)