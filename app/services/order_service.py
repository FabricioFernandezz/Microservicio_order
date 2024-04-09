from app.repositories import OrderRepository

class OrderService:
    
    def __init__(self):
        self.__repo = OrderRepository()

    def find_by_id(self, id_order):
        return self.__repo.find_by_id(id_order)
    
    def find_all(self):
        return self.__repo.find_all()
    
    def update (self, order, id_order):
        return self.__repo.update(order, id_order)
    
    def delete(self, id_order):
        return self.__repo.delete(id_order)
        
    def create(self, order):
        return self.__repo.create(order)