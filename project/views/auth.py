import calendar
import datetime

import jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from project.config import BaseConfig
from project.dao.models import User
from project.implemented import user_service

from project.setup_db import db
from project.tools.security import generate_password_digest

SECRET = BaseConfig.SECRET_KEY
ALGO = BaseConfig.ALGO
MINUTES = BaseConfig.TOKEN_EXPIRE_MINUTES
DAYS = BaseConfig.TOKEN_EXPIRE_DAYS

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            abort(400)

        user = db.session.query(User).filter(User.email == email).first()

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        password_hash = generate_password_digest(password).decode("utf-8", "ignore")

        if password_hash != user.password:
            return {"error": "Неверные учётные данные, пароль"}, 401

        data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
        }
        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=MINUTES)
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=DAYS)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(400)

        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=ALGO)
        except Exception as e:
            abort(400)

        email = data.get("email")

        user = db.session.query(User).filter(User.email == email).first()

        data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
        }
        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=MINUTES)
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=DAYS)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201
