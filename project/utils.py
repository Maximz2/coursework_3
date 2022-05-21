import json

import jwt
from flask import request, abort

from project.views.auth import SECRET, ALGO


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[ALGO])
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def decode_token(token):
    try:
        data = jwt.decode(token, SECRET, algorithms=[ALGO])
        return data['id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again'


def get_id_by_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        token = ''
    uid = decode_token(token.encode())
    return uid
