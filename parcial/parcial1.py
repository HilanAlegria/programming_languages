from functools import reduce

def lazy_load_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Leer
        header = f.readline().strip().split(',')
        # Repetir sobre cada línea del archivo
        for line in f:
            values = line.strip().split(',')
            
            # Convertir canpos numéricos a int (nivel, ataque, defensa)
            record = dict(zip(header, values))
            record['nivel'] = int(record['nivel'])
            record['ataque'] = int(record['ataque'])
            record['defensa'] = int(record['defensa'])
            
            yield record

if __name__ == "__main__":
    # Carga de datos
    characters_gen = lazy_load_characters("C:/Users/estudiante/Downloads/lenguajes-de-programaci-n--main/lenguajes-de-programaci-n--main/lenguajes de programacion/python/parcial/personajes.csv")
    
    filtered_characters = filter(lambda c: c['nivel'] > 10, characters_gen)
    #totalpower ataque + defenza 
    mapped_characters = map(lambda c: {**c, "totalPower": c['ataque'] + c['defensa']}, filtered_characters)
    
    strongest = reduce(lambda a, b: a if a['totalPower'] > b['totalPower'] else b, mapped_characters)
    
    print("Personaje con mayor poder total:", strongest)
    #personaje extra cargado al csv :D