from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        director = self.dao.get_by_id(pk)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = self.dao.get_all()
        return DirectorSchema(many=True).dump(directors)
