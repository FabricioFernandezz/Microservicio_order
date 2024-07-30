from sqlalchemy import Column, Integer, String, Float
from app import db

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Float)
    brand = Column(String(50))
    size = Column(String(50))
    stock = Column(Float)

    def __init__(self, name, price, brand, size, stock):
        self.name = name
        self.price = price
        self.brand = brand
        self.size = size
        self.stock = stock
