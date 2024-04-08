from flask import Blueprint, jsonify, request
from app.services.order_service import OrderService
from app.mapping.order_schema import OrderSchema

schema = OrderSchema()
order=Blueprint('order', __name__)

