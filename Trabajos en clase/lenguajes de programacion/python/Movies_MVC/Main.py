from Model import *
from Movies_MVC import MovieRepository
from Movies_MVC.Repositories.mongodb_repository import MongoDBRepository


# principio "L": principio de sustitucion de Liskov: puedes usarse una subclase en reemplazo de su superclase
# sin afectar el funcionamiento del modulo o dle sistema completo:
repo: MovieRepository = MongoDBRepository()
lista_todas_peliculas = repo.get_all()
