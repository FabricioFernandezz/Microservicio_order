from app.services.order_service import *

class OrderService:
    def __init__(self):
        self.order_service = OrderService()

    def find_all(self):
        return self.order_service.find_all()

    def find_by_id(self, id):
        return self.order_service.find_by_id(id)

    def create(self, order):
        return self.order_service.create(order)

    def update(self, order):
        return self.order_service.update(order)

    def delete(self, id):
        return self.order_service.delete(id)