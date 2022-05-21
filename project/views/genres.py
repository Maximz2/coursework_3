from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.implemented import genre_service

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        return genre_service.get_all_genres()


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Get genre by id"""
        try:
            return genre_service.get_item_by_id(genre_id)
        except ItemNotFound:
            abort(404, message="Genre not found")
