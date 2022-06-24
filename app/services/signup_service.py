from flask import make_response, jsonify
from app.helper.validations import email_validation, password_validation
from extensions import app
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash
from app.models import query_builder
import uuid
from datetime import datetime

error_pwd_validation_msg = 'Password must contain at least 6 characters, including Upper/Lowercase, special characters and numbers'


def user_signup(request):
    app.logger.info(f"signup: In a sing_up route and inputs from route {request}")
    try:
        username = request.form['username']

        search_user = query_builder.find(username)
        if search_user == True:
            return make_response(jsonify({"username": username + ' username already exists'}), 400)

        email = request.form['email']
        if email_validation(email) == None:
            return make_response(jsonify({"email_validation": email + ' is not a valid email address'}), 400)

        password = request.form['password']
        if password_validation(password) == None:
            return make_response(jsonify({"password_validation": error_pwd_validation_msg}), 400)

        user = {}

        user['user_id'] = str(uuid.uuid4())
        user['username'] = username
        user['password'] = generate_password_hash(password)
        user['name'] = request.form['name']
        user['email'] = email
        user['dob'] = request.form['dob']
        user['created_at'] = datetime.now()

        got_data = query_builder.add_one_file(user)

    except KeyError:
        abort(400)
    return make_response(jsonify({
        "success": 'User Created Successfully'
    }), 201)
