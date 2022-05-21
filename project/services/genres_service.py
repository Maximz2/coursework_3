from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        genre = self.dao.get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = self.dao.get_all()
        return GenreSchema(many=True).dump(genres)
