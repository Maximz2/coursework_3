from project.dao import UserDAO
from project.services.base import BaseService
from project.tools.security import generate_password_digest


def get_hash(password):
    return generate_password_digest(password).decode("utf-8", "ignore")


class UsersService(BaseService):
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, user_d):
        user_d['password'] = get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self,  user, name, surname, favorite_genre):
        self.dao.update(user, name, surname, favorite_genre)

    def update_password(self,  user, password_1, password_2):
        password_1 = get_hash(password_1)
        password_2 = get_hash(password_2)
        if user.password == password_1:
            self.dao.update(user, password=password_2)

