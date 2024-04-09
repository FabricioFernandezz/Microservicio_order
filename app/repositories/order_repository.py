from app.models.order import *
from app.repositories.base_repository import BaseRepository
from app.config.database import db
from app import db

class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Order)
        self.__model = Order

    def update(self, entity: db.Model, id: int):
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