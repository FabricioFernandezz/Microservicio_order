from app.models.order import *
from app.repositories.base_repository import BaseRepository
from app import db

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Order)
        self.__model = Order

    def create(self, entity: Order):
        try:
            db.session.add(entity)
            db.session.commit()
            db.session.refresh(entity) 
            return entity
        except Exception as e:
            db.session.rollback()
            raise e
        
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id: int):
        return db.session.query(self.__model).get(id)
    
    def delete(self, id: int):
        try:
            entity = db.session.query(self.__model).get(id)
            if entity:
                db.session.delete(entity)
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            db.session.rollback()
            raise e
        
    def update(self, entity: Order, id: int):
        try:
            existing_entity = db.session.query(self.__model).get(id)
            if existing_entity :
                existing_entity.id_client = entity.id_client
                existing_entity.id_product = entity.id_product
                existing_entity.payment_method = entity.payment_method
                existing_entity.total = entity.total
                db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e