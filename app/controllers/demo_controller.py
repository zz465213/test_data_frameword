# app/controllers/user_account_controller.py
from flask import Blueprint, request, jsonify
from app.services.demo_service import DemoService
from flasgger import swag_from  # 用於 Swagger 文件生成

demo_bp = Blueprint('user_account', __name__)
demo_service = DemoService()


@demo_bp.route('/create_accounts', methods=['POST'])
@swag_from({
    'tags': ['User Accounts'],
    'parameters': [
        {
            'name': 'user_id',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'The ID of the user to create accounts for.'
        }
    ],
    'responses': {
        200: {
            'description': 'Accounts created successfully.',
            'schema': {'type': 'object', 'properties': {'message': {'type': 'string'}}}
        },
        400: {
            'description': 'Invalid input.',
            'schema': {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        }
    }
})
def create_user_accounts():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        demo_service.insert_member_and_account(user_id)
        return jsonify({'message': f'Accounts created for user {user_id}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
