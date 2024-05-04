import random  # Para seleccionar elementos aleatorios
import json  # Para exportar el resultado a JSON
from faker import Faker  # Para generar nombres aleatorios
import sys


faker = Faker()
# inicializa la clase faker para crear datos ficticios

# lista de ciudades europeas permitidas
ciudades = [
    {"name": "Paris", "lat_range": (48.8, 49.1), "long_range": (2.2, 2.6)},
    {"name": "Amsterdam", "lat_range": (52.3, 52.5), "long_range": (4.7, 5.0)},
    {"name": "Munich", "lat_range": (48.1, 48.2), "long_range": (11.4, 11.7)},
    {"name": "London", "lat_range": (51.4, 51.6), "long_range": (-0.2, 0.2)},
    {"name": "Madrid", "lat_range": (40.3, 40.5), "long_range": (-3.8, -3.6)},
    {"name": "Florence", "lat_range": (43.7, 43.8), "long_range": (11.2, 11.4)},
    {"name": "Vienna", "lat_range": (48.1, 48.3), "long_range": (16.3, 16.6)},
    {"name": "Lisbon", "lat_range": (38.7, 38.8), "long_range": (-9.2, -9.0)},
    {"name": "Budapest", "lat_range": (47.3, 47.5), "long_range": (19.0, 19.1)},
    {"name": "Barcelona", "lat_range": (41.3, 41.5), "long_range": (2.1, 2.3)},
    {"name": "Rome", "lat_range": (41.8, 41.9), "long_range": (12.4, 12.5)},
    {"name": "Zurich", "lat_range": (47.3, 47.4), "long_range": (8.5, 8.7)},
    {"name": "Prague", "lat_range": (50.0, 50.1), "long_range": (14.3, 14.5)},
    {"name": "Berlin", "lat_range": (52.5, 52.6), "long_range": (13.3, 13.5)},
    {"name": "Dublin", "lat_range": (53.3, 53.4), "long_range": (-6.3, -6.1)},
    {"name": "Milan", "lat_range": (45.4, 45.5), "long_range": (9.1, 9.3)},
    {"name": "Brussels", "lat_range": (50.8, 50.9), "long_range": (4.3, 4.5)},
]

# lista de categorías posibles para los restaurantes
categorias = [
    "italian",
    "mediterranean",
    "mexican",
    "vegan",
    "japanese",
    "sushi",
    "france",
    "spanish",
    "portuguese",
    "austriac",
    "tapes",
    "latin",
    "pizza",
    "european",
    "barbaque",
    "asian",
    "pasta",
]

categories_graph = {
    "italian": ["mediterranean", "pasta"],
    "mediterranean": [
        "spanish",
        "portuguese",
        "italian",
        "pasta",
        "european",
        "france",
    ],
    "mexican": ["latin"],
    "vegan": [],
    "japanese": ["sushi", "asian"],
    "sushi": ["japanese", "asian"],
    "france": ["european"],
    "spanish": ["tapes", "european", "mediterranean"],
    "portuguese": ["european", "mediterranean"],
    "austriac": ["european"],
    "tapes": ["spanish"],
    "latin": ["mexican"],
    "pizza": ["italian"],
    "european": ["spanish", "portuguese", "pasta", "mediterranean", "france"],
    "barbaque": [],
    "asian": ["sushi", "japanese"],
    "pasta": ["mediterranean"],
}


# función para generar un restaurante aleatorio
def generar_restaurante():
    nombre = faker.company()  # Generar un nombre ficticio
    ciudad = random.choice(ciudades)  # Elegir una ciudad aleatoria
    num_categorias = random.choice(
        [_ for _ in range(1, 4)]
    )  # Elegir si tiene 1 o 2 categorías
    aux_list = random.sample(categorias, 1)  # Elegir categorías aleatorias
    categorias_restaurante = []

    category = aux_list[0]
    categorias_restaurante.append(category)
    aux_list = aux_list + categories_graph[category]
    num_categorias -= 1

    while num_categorias > 0 and aux_list:
        if aux_list[0] not in categorias_restaurante:
            category = aux_list[0]
            categorias_restaurante.append(category)
            aux_list = aux_list + categories_graph[category]
            num_categorias -= 1
        aux_list = aux_list[1::]
    # comida_popular = random.choice([True, False])  # Decidir si sirve comida popular

    latitud = random.uniform(ciudad["lat_range"][0], ciudad["lat_range"][1])
    longitud = random.uniform(ciudad["long_range"][0], ciudad["long_range"][1])

    hora_apertura = random.randint(8, 11)  # Apertura entre las 8 y las 11 a.m.
    hora_cierre = random.randint(18, 23)  # Cierre entre las 6 y las 11 p.m.

    return {
        "restaurant ID": 0,
        "name": nombre,
        "category": categorias_restaurante,
        "city": ciudad,
        "latitude": latitud,
        "longitude": longitud,
        "opening_hours": {"open": hora_apertura, "close": hora_cierre},
        # "comida_popular": comida_popular
    }


# Generar una lista de restaurantes
def generar_lista_restaurantes(num_restaurantes):
    restaurantes = [generar_restaurante() for _ in range(num_restaurantes)]
    for x in range(len(restaurantes)):
        restaurantes[x]["restaurant ID"] = x
    return restaurantes


def main():
    if len(sys.argv) != 2:
        print("usage: python3 restaurantsgenerator.py <num-restaurants>")
        return
    # Ejemplo: generar 10 restaurantes aleatorios
    restaurantes_aleatorios = generar_lista_restaurantes(int(sys.argv[1]))

    # Convertir la lista a JSON
    with open("dataset/restaurants.json", "w", encoding="utf-8") as f:
        json.dump(restaurantes_aleatorios, f, ensure_ascii=False, indent=4)
        print("json file generated")


main()
