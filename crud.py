#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import utils

DATABASE = 'database/main.db'

conn = None
def connect():
    try:
        global conn
        conn = sqlite3.connect(DATABASE)
    except Exception:
        print Exception.message

def insert_user(user):
    global conn
    if(conn == None):
        connect()
    try:
        conn.execute('INSERT INTO user (nameUser, passwordUser) VALUES (?, ?)', [user['user'], user['password']])
    except sqlite3.IntegrityError:
        print 'Usuário ja cadastrado'
        return '800'
    conn.commit()
    return '200'

def select_user_byName(user_name):
    try:
        global conn
        if (conn == None):
            connect()
        cursor = conn.execute('SELECT * FROM user where nameUser = ?', [user_name])
        return take_user(cursor)
    except sqlite3.DataError:
        print 'Usuário não encontrado'
        return '801'

def select_user_byID(user_id):
    try:
        global conn
        if (conn == None):
            connect()
        cursor = conn.execute('SELECT * FROM user where idUser = ?', [user_id])
        return take_user(cursor)
    except sqlite3.DataError:
        print 'Usuário não encontrado'
        return '801'

def take_user(cursor):
    for row in cursor:
        user = utils.user_to_json(row)
        return user
