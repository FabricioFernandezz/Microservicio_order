from app.repositories import OrderRepository
from app import cache

class OrderService:
    
    def __init__(self):
        self.__repo = OrderRepository()

    def find_by_id(self, id_order):
        order = cache.get(f'{id_order}')
        if order is None:
            order = self.__repo.find_by_id(id_order)
            cache.set(f'{id_order}', order, timeout=60)
        return order
    
    def find_all(self):
        return self.__repo.find_all()
    
    def update(self, order, id_order):
        return self.__repo.update(order, id_order)
    
    def delete(self, id_order):
        return self.__repo.delete(id_order)
        
    def create(self, order):
        created_order = self.__repo.create(order)
        cache.set(f'{created_order.id_order}', created_order, timeout=60)
        return created_order