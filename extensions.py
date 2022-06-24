from flask import Flask, jsonify
from flask_pymongo import PyMongo
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


# common exception Handler for whole app or all routes function
def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception

    @wraps(handle_http_exception)
    def ret_val(exception):
        exc = handle_http_exception(exception)
        return jsonify({'code': exc.code, 'message': exc.description}), exc.code
    return ret_val


# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)


app.config['HOST'] = os.getenv('HOST')
app.config['PORT'] = os.getenv('PORT')

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['COLLECTION'] = os.getenv('COLLECTION')
mongodb_client = PyMongo(app)
db = mongodb_client.db
collection = db[app.config['COLLECTION']]
