from abc import ABC, abstractmethod

from app.models.order import Order

class Create(ABC):
    @abstractmethod
    def create(self, entity:Order):
        pass

class Read(ABC):
    @abstractmethod
    def find_by_id(self, id:int):
        pass

class Update(ABC):
    @abstractmethod
    def update(self, entity:Order, id:int):
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, entity:Order):
        pass