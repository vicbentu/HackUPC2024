import random  # Para seleccionar elementos aleatorios
import json  # Para exportar el resultado a JSON
from faker import Faker  # Para generar nombres aleatorios
import sys


faker = Faker()
# inicializa la clase faker para crear datos ficticios

# lista de ciudades europeas permitidas
ciudades = [
    "Paris", "Amsterdam", "Munich", "London", "Madrid", "Florence",
    "Vienna", "Lisbon", "Budapest", "Barcelona", "Rome", "Zurich",
    "Prague", "Berlin", "Dublin", "Milan", "Brussels"
]

# lista de categorías posibles para los restaurantes
categorias = [
    "italian", "mediterranean", "mexican", "vegan", "japanese",
    "sushi", "france", "spanish", "portuguese", "austriac", "tapes", "latin",
    "pizza", "european", "barbaque", "asian", "pasta"
]

categories_graph = {
    "italian": ["mediterranean", "pasta"],
    "mediterranean": ["spanish", "portuguese", "italian", "pasta", "european", "france"],
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
    "pasta": ["mediterranean"]
}

# función para generar un restaurante aleatorio
def generar_restaurante():
    nombre = faker.company()  # Generar un nombre ficticio
    ciudad = random.choice(ciudades)  # Elegir una ciudad aleatoria
    num_categorias = random.choice([_ for _ in range(1, 4)])  # Elegir si tiene 1 o 2 categorías
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
    
    return {
        "restaurant ID" : 0,
        "name": nombre,
        "category": categorias_restaurante,
        "city": ciudad
        # "comida_popular": comida_popular
    }

# Generar una lista de restaurantes
def generar_lista_restaurantes(num_restaurantes):
    restaurantes = [generar_restaurante() for _ in range(num_restaurantes)]
    for x in range(len(restaurantes)):
        restaurantes[x]['restaurant ID'] = x
    return restaurantes

def main():
    if len(sys.argv) != 2:
        print('usage: python3 restaurantsgenerator.py <num-restaurants>')
        return
    # Ejemplo: generar 10 restaurantes aleatorios
    restaurantes_aleatorios = generar_lista_restaurantes(int(sys.argv[1]))

    # Convertir la lista a JSON
    with open('dataset/restaurants.json', 'w', encoding='utf-8') as f:
        json.dump(restaurantes_aleatorios, f, ensure_ascii=False, indent=4)
        print("json file generated")

main()
