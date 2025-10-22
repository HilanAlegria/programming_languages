from movie_repository import MovieRepository

# se aplica la "o" de los principios SOLID: casa repositorio concreto, implementa las operaciones para un store
# especifico 
class MongoDBRepository(MovieRepository):
    
    def get_all(this):
        #return super().get_all()
        return[
        {"title":"Fast & Furious Five", "year":2011, "genre":"cars & action", "director":"Vine Disel"},
        {"title":"Kimetsu No Yaiba", "year":2025, "genre":"ciencia ficcion", "director":"Haruo Sotozaki"},
    ]