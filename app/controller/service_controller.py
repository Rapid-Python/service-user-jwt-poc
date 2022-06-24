from flask import request, Blueprint, jsonify
from extensions import app
from app.services import signup_service, users, login_service

api = Blueprint('user', 'user')


@api.route('/signup', methods=['POST'])
def signup():
    app.logger.info(f"signup: Inputs from route {request}")
    return signup_service.user_signup(request)


@api.route('/login', methods=['POST'])
def login():
    app.logger.info(f"login: Inputs from route login credentials {request}")
    return login_service.user_login(request)


@api.route('/get_user', methods=['GET'])
def get_user():
    app.logger.info(f"get_user: In a current user route")
    return users.user_profile()


@api.route('/get_all_user', methods=['GET'])
def get_all_user():
    app.logger.info(f"get_all_user: In a get all user route")
    return users.get_alluser()
