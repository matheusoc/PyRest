#!/usr/bin/python
# -*- coding: utf-8 -*-

def user_to_json(user):
    return {
        "user_id": user[0],
 	    "user": user[1],
        "password": user[2]
    }
