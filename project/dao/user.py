from project.dao.models import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, user: User, name=None, surname=None, favorite_genre=None, password=None):
        if name:
            user.name = name
        if surname:
            user.surname = surname
        if favorite_genre:
            user.favorite_genre = favorite_genre
        if password:
            user.password = password
        self.session.commit()
