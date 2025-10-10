from Model.Vehicle import Vehicle
from View.VehicleView import VehicleView
from Repositories.Vehicle_repository import VehicleRepository


class MovieController:
    
    def __init__(self, repository: VehicleRepository, view: VehicleView):
        self.repository = repository
        self.view = view
        
    # implementacion de una funcion de CRUD que seria llamada desde la vista
    # O le reporaria a la vista
    
    def listAllMovies(self):
        moviesData = self.repository.get_all()
        # visualiza la informacion a travez del view:
        self.view.showMovies(moviesData)