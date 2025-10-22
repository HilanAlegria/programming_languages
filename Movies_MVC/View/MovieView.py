class MovieView:
    
    def showMovies(this, movies):
        print("Esta es la lista de peliculas\n")
        for m in movies:
            print(f"-{m.title} ({m.year}) - {m.genre}, dir: {m.director}")
