from Model.movie import Movie
from View.MovieView import MovieView
from Repositories.movie_repository import MovieRepository


class MovieController:
    
    def __init__(self, repository: MovieRepository, view: MovieView):
        self.repository = repository
        self.view = MovieView
        
    # implementacion de una funcion de CRUD que seria llamada desde la vista
    # O le reporaria a la vista
    def listAllMovies(self):
        moviesData = self.repository.get_all()
        # visualiza la informacion a travez del view:
        self.view.showMovies(moviesData)
        