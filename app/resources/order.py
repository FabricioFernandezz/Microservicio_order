from flask import Blueprint, jsonify, request
from app.services.order_service import OrderService
from app.mapping.order_schema import OrderSchema

schema = OrderSchema()
order=Blueprint('order', __name__)

@order.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    order = schema.load(data)
    order_service = OrderService()
    created_order = order_service.create_order(order)
    result = schema.dump(created_order)
    return jsonify(result), 201

@order.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    order_service = OrderService()
    order = order_service.get_order(order_id)
    result = schema.dump(order)
    return jsonify(result), 200

@order.route('/order/<order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order = schema.load(data)
    order_service = OrderService()
    updated_order = order_service.update_order(order_id, order)
    result = schema.dump(updated_order)
    return jsonify(result), 200

@order.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    order_service = OrderService()
    order_service.delete_order(order_id)
    return jsonify({'message': 'Order deleted'}), 200