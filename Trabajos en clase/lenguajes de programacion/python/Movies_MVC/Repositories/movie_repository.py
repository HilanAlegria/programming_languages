from abc import ABC, abstractmethod

# define como controlas las operciones de CRUD
class MovieRepository(ABC):
    
    @abstractmethod
    def get_all(this):
        pass
    
# principio "I": interface seggregation principle: se separan comportamientos genrales distintos
# en varias interfaces, en vez de empacarlas en una sola     
# las subclases implementan solo lo que vayan a usar 
class IReadableRepository(ABC):
    
    @abstractmethod
    def read_all(this):
        pass
    
class IWritableRepository(ABC):
    
    @abstractmethod
    def save_item(this, item):
        pass
    
    