from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.implemented import director_service


directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        return director_service.get_all_directors()


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, director_id: int):
        """Get director by id"""
        try:
            return director_service.get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
