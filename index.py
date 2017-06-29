#!/usr/bin/python
#coding=utf-8

from flask import Flask, request
import crud
import json
from Hello import testing

app = Flask(__name__)
app.register_blueprint(testing)

session = []

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        user = json.loads(request.data.decode())
        response = crud.insert_user(user)
        return response


@app.route('/login', methods=['POST'])
def login():
    """Logs the user in."""
    data = json.loads(request.data.decode())
    user = crud.select_user_byName(data['user'])
    global session
    for i in session:
        if i == user['user_id']:
            if data['password'] == user['password']:
                return "{'status': 'alogged'}"
            session.remove(user['user_id'])

    if request.method == 'POST':
        if user is None:
            error = "{'status':'Usuário incorreto'}"
        elif not (data['password'] == user['password']):
            error = "{'status':'Senha incorreta'}"
        else:
            session.append(user['user_id'])
            return "{'status': 'logged'}"
    return error

@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        global session
        data = json.loads(request.data.decode())
        user = crud.select_user_byName(data['user'])
        if len(session) > 0:
            try:
                session.remove(user['user_id'])
                return 'logged out'
            except ValueError:
                print 'Not at the list'
        return 'not logged'

if __name__ == '__main__':
    app.run(debug=True)
