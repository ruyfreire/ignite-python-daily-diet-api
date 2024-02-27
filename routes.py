from flask import Blueprint, jsonify, request
from models.diet import Diet, create_diet_db, get_all_diets_db, get_diets_db, delete_diet_db, update_diet_db
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

    success = create_diet_db(diet)
    if success:
        return jsonify({'message': 'Diet created successfully'}), 201
    
    return jsonify({'message': 'Error to create Diet'}), 500

@diet_routes.route('/diet', methods=['GET'])
def get_diet():
    diets = get_all_diets_db()

    return jsonify({"diets": [diet.serialize() for diet in diets]}), 200

@diet_routes.route('/diet/<uuid:diet_id>', methods=['GET'])
def get_diet_by_id(diet_id: str):
    diet = get_diets_db(diet_id)

    if not diet:
        return jsonify({'message': 'Diet not found'}), 404

    return jsonify({"diet": diet.serialize()}), 200

@diet_routes.route('/diet/<uuid:diet_id>', methods=['PUT'])
def update_diet_by_id(diet_id: str):
    diet = get_diets_db(diet_id)

    if not diet:
        return jsonify({'message': 'Diet not found'}), 404
    
    body = request.json

    name = body.get('name')
    description = body.get('description')
    date = body.get('date')
    is_diet = body.get('is_diet')

    diet_to_update = Diet(
        name=diet.name,
        description=diet.description,
        date=diet.date,
        is_diet=diet.is_diet
    )

    if name:
        diet_to_update.name = name

    if description:
        diet_to_update.description = description

    if date:
        diet_to_update.date = date

    if is_diet == True or is_diet == False:
        diet_to_update.is_diet = is_diet

    success = update_diet_db(diet_id, diet_to_update)

    if not success:
        return jsonify({'message': 'Error to update Diet'}), 500

    return jsonify({'message': 'Diet updated successfully'}), 200

@diet_routes.route('/diet/<uuid:diet_id>', methods=['DELETE'])
def delete_diet_by_id(diet_id: str):
    deleted = delete_diet_db(diet_id)

    if not deleted:
        return jsonify({'message': 'Diet not found'}), 404

    return jsonify({'message': 'Diet deleted successfully'}), 200
