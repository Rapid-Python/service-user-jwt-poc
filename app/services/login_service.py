from flask import request, jsonify, make_response, app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from extensions import app
from app.models import query_builder
import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def user_login(request):
    # auth = request.form
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )
    email = auth.get('email')
    user = query_builder.find_email(email)

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify the user',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )

    passcode = query_builder.password(email)
    hash_password = passcode['password']
    user_id = passcode['user_id']

    if check_password_hash(hash_password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(seconds=240)
        }, app.config['SECRET_KEY'])

        return jsonify(({'token': token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify the password',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    )
