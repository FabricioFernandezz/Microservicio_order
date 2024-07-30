from app.repositories import OrderRepository
from app import cache
from tenacity import retry, stop_after_attempt, stop_after_delay

class OrderService:
    
    def __init__(self):
        self.__repo = OrderRepository()

    def find_by_id(self, id_order):
        order_id = cache.get(f'{id_order}')
        if order_id is None:
            order_id = self.__repo.find_by_id(id_order)
            cache.set(f'{id_order}', order_id, timeout=60)
        return order_id
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def find_all(self):
        find_all_orders = cache.get('find_all_orders')
        if find_all_orders is None:
            find_all_orders = self.__repo.find_all()
            cache.set('find_all_orders', find_all_orders, timeout=60)
        return self.__repo.find_all()
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def update(self, order_data, id_order):
        existing_order = self.find_by_id(id_order)
        if not existing_order:
            return None  
        
        updated_order = self.__repo.update(order_data, id_order)
        if updated_order:
            cache.set(f'{id_order}', updated_order, timeout=60)
        return updated_order
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def delete(self, id_order):
        cache.delete(f'{id_order}')
        return self.__repo.delete(id_order)
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def create(self, order):
        created_order = self.__repo.create(order)
        cache.set(f'{created_order.id_order}', created_order, timeout=60)
        return created_order