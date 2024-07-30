from app import db
from dataclasses import dataclass
from sqlalchemy import Column

@dataclass
class Client(db.Model):
    __tablename__ = 'client'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    name = Column(db.String(50))
    surname = Column(db.String(50))
    phone_number = Column(db.String(50))
    email = Column(db.String(50))
    dni= Column(db.String(50))
    address = Column(db.String(50))
    password = Column(db.String(50))

    def __init__(self, name, surname, phone_number, email, dni, address, password):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.dni = dni
        self.address = address
        self.password = password