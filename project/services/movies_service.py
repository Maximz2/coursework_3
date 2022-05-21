from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.services.base import BaseService


class MoviesService(BaseService):
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        movie = self.dao.get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all_movies(self):
        movies = self.dao.get_all()
        return MovieSchema(many=True).dump(movies)

    def get_all_movies_by_status(self):
        movies = self.dao.get_all_by_status()
        return MovieSchema(many=True).dump(movies)