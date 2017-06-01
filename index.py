#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
import crud
import json

app = Flask(__name__)

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
            return 'alogged'

    if request.method == 'POST':
        if user is None:
            error = 'Invalid username'
        elif not (data['password'] == user['password']):
            error = 'invalid password'
        else:
            session.append(user['user_id'])
            return 'logged'
    return 'Error to login: ' + error

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
    app.run(host='192.168.1.3', debug=True)