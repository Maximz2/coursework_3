from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.implemented import movie_service

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        pagination = request.args.get('page')
        status = request.args.get('status')
        if status and status == "new":
            all_movies = movie_service.get_all_movies_by_status()
        else:
            all_movies = movie_service.get_all_movies()
        all_movies = all_movies[:int(pagination)] if pagination else all_movies
        return all_movies


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return movie_service.get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
