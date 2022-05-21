from project.config import DevelopmentConfig
from project.dao.models import Genre, Director, Movie, User
from project.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre, "Director": Director, "Movie": Movie, "User": User
    }


app.debug = True


if __name__ == '__main__':
    app.run(host="localhost")
