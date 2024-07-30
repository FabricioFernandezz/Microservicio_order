from dataclasses import dataclass
from app import db
from dataclasses import dataclass

@dataclass
class Order(db.Model):
    __tablename__ = 'orders'
    id_order = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column("id_client", db.Integer, db.ForeignKey('client.id'))
    id_product = db.Column("id_product", db.Integer, db.ForeignKey('product.id'))
    payment_method = db.Column("payment_method", db.String(50))
    total = db.Column("total", db.String(50))

    def __init__(self, id_client,id_product, payment_method, total):
        self.id_client = id_client
        self.id_product = id_product
        self.payment_method = payment_method
        self.total = total

