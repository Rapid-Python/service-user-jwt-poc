from extensions import app, db, collection
from flask import jsonify


# query function to add one document to database collection
def add_one_file(request_data):
    app.logger.info(f"user_data: add file route got called")
    collection.insert_one(request_data)
    return jsonify({"status_code": 200, "message": "successfully Inserted"})


def find(username):
    app.logger.info(f"user_data: user search in database")
    if collection.find_one({'username': username}):
        return True
    else:
        return False


def search_one_user(user_id):
    app.logger.info(f"user_data: user search in database")
    user = collection.find_one({'user_id': user_id})
    return user


def get_all_list():
    app.logger.info(f"UploadFile: getlist route got called")
    document = collection.find()
    temp_list = []
    for i, obj in enumerate(document):
        obj["_id"] = str(obj["_id"])
        temp_list.append(obj)
    return temp_list


def find_email(email):
    app.logger.info(f"user_data: user search in database")
    if collection.find_one({'email': email}):
        return True
    else:
        return False


def password(email):
    app.logger.info(f"user_data: user search in database")
    user = collection.find_one({'email': email})
    return user


def user_verify(user_id):
    app.logger.info(f"user_data: user search in database")
    user = collection.find_one({'user_id': user_id})
    return user
