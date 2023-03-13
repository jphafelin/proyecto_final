"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Participante, Monitor, Evento, Participantes_de_Eventos, Tipo_de_Evento
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['GET'])
def user():
    if request.method == "GET":
        users = User.query.all()
        results = [user.serialize() for user in users]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200
 
    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400


@api.route('/participante', methods=['GET'])
def funcionparticipante():
    if request.method == "GET":
        participantes = Participante.query.all()
        results = [participanteserialize.serialize() for participanteserialize in participantes]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200
 
    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400


@api.route('/monitor', methods=['GET'])
def funcionmonitor():
    if request.method == "GET":
        monitores = Monitor.query.all()
        results = [monitorserialize.serialize() for monitorserialize in monitores]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200
 
    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400


@api.route('/evento', methods=['GET'])
def evento():
    if request.method == "GET":
        eventos = Evento.query.all()
        results = [evento.serialize() for evento in eventos]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200

    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400


@api.route('/tipo-de-evento', methods=['GET'])
def tiposdeeventos():
    if request.method == "GET":
        tipo_de_evento = Tipo_de_Evento.query.all()
        results = [tipo.serialize() for tipo in tipo_de_evento]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200

    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400

@api.route('/participantes', methods=['GET'])
def participantes():
    if request.method == "GET":
        participantes_evento = Participantes_de_Eventos.query.all()
        results = [participante.serialize() for participante in participantes_evento]
        response_body = {"message": "ok",
                        "results": results,
                        "Total_records": len(results)}
        return response_body, 200

    else:
        response_body = {"message": "Error. Method not allowed."}
        return response_body, 400


