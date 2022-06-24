from flask import make_response, jsonify
from app.models import query_builder
from app.helper.jwt_token_validator import token_required


@token_required
def user_profile(current_user):
    user = query_builder.search_one_user(current_user)
    return jsonify({'status_code': 200, 'message': 'Successfully fetched', 'current_user': str(user)})


@token_required
def get_alluser(current_user):
    user = query_builder.get_all_list()
    return jsonify({'status_code': 200, 'message': 'Successfully fetched', 'list': user})

