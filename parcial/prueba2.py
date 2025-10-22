from functools import reduce

def lazy_load_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            record = dict(zip(header, values))
            record['nivel'] = int(record['nivel'])
            record['ataque'] = int(record['ataque'])
            record['defensa'] = int(record['defensa'])
            yield record

if __name__ == "__main__":
    characters_gen = lazy_load_characters("C:/Users/estudiante/Downloads/lenguajes-de-programaci-n--main/lenguajes-de-programaci-n--main/lenguajes de programacion/python/parcial/personajes.csv")

    filtered_characters = filter(lambda c: c['nivel'] > 10, characters_gen)
    mapped_characters = map(lambda c: {**c, "totalPower": c['ataque'] + c['defensa']}, filtered_characters)

    # Convertir a lista para poder ordenar
    characters_list = list(mapped_characters)

    # Ordenar desc por totalPower
    characters_list.sort(key=lambda c: c['totalPower'], reverse=True)

    # Obtener los 3 personajes más poderosos
    top_3 = characters_list[:3]

    print("Los 3 personajes con mayor poder total son:")
    for i, character in enumerate(top_3, start=1):
        print(f"{i}. {character}")
