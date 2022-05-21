from project.dao import DirectorDAO, GenreDAO, MovieDAO, UserDAO
from project.services import DirectorsService, GenresService, MoviesService, UsersService
from project.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
