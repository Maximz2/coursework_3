from flask import request
from flask_restx import Resource, Namespace

from project.implemented import user_service
from project.schemas.user import UserSchema
from project.utils import auth_required, decode_token, get_id_by_token

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        uid = get_id_by_token()
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    @auth_required
    def patch(self):
        uid = get_id_by_token()
        user = user_service.get_one(uid)
        req_json = request.json
        name = req_json.get("name", None)
        surname = req_json.get("surname", None)
        favorite_genre = req_json.get("favorite_genre", None)
        user_service.update(user, name, surname, favorite_genre)
        return "", 204


@user_ns.route('/password')
class UserView(Resource):

    @auth_required
    def put(self):
        uid = get_id_by_token()
        user = user_service.get_one(uid)
        req_json = request.json
        password_1 = req_json.get("password_1", None)
        password_2 = req_json.get("password_2", None)
        user_service.update_password(user, password_1, password_2)
        return "", 204
