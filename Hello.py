from flask import Flask, request, Blueprint
import json

testing = Blueprint('testing', __name__)

@testing.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET':
        return 'Hello Moto'
