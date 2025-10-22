from Controller.movie_controller import MovieController
from View.MovieView import MovieView
from Repositories.mongodb_repository import MongodbRepository


if __name__ == "__main__":
    repo = MongodbRepository()
    view = MovieView()
    controller = MovieController(repo, view)
    controller.listAllMovies()