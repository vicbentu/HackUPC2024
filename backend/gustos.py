import csv
import os
import random

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


# Función para generar las categorías favoritas de restaurantes para una persona
def generar_gustos():
    num_gustos = random.randint(1, 3)  # Entre 1 y 3 gustos aleatorios
    return random.sample(categorias, num_gustos)  # Seleccionar gustos aleatorios


# Ruta del archivo CSV de entrada y salida
input_csv = "./dataset/hackupc-travelperk-dataset.csv"
output_csv = os.path.join("dataset", "output.csv")

# Leer el archivo CSV de entrada y crear el nuevo archivo CSV con la columna adicional
with open(input_csv, "r", newline="") as infile, open(
    output_csv, "w", newline=""
) as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["favorite_categories"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row["favorite_categories"] = ", ".join(generar_gustos())
        writer.writerow(row)

print(
    f"Se ha creado el archivo CSV '{output_csv}' con la nueva columna 'favorite_categories'."
)
