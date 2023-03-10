"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == "GET":
        users = User.query.all()
        results = [user.serialize() for user in users]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200
    elif request.method == "POST":
        request_body = request.get_json()
        user = User(email = request_body['email'],
                    password = request_body['password'])
        db.session.add(user)
        db.session.commit()
        response_body = {"details": request_body,
                         "message": "User created"}
        return response_body, 200
    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400