from flask import Blueprint, jsonify, request
from models.diet import Diet, create_diet_db, get_all_diets_db
import datetime

diet_routes = Blueprint('diet', __name__)

@diet_routes.route('/diet', methods=['POST'])
def create_diet():
    body = request.json

    name = body.get('name')
    description = body.get('description', '')
    date = body.get('date', datetime.datetime.now())
    is_diet = body.get('is_diet', False)

    if not name:
        return jsonify({'message': 'Name is required'}), 400
    
    diet = Diet(name=name, description=description, date=date, is_diet=is_diet)

    result = create_diet_db(diet)

    if result:
        return jsonify({'message': 'Diet created successfully'}), 201
    
    return jsonify({'message': 'Error to create Diet'}), 500

@diet_routes.route('/diet', methods=['GET'])
def get_diet():
    diets = get_all_diets_db()

    return jsonify({"diets": diets}), 200
