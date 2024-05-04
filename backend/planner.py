# tener en cuenta:
# proximidad de restaurantes
# horarios de apertura y cierre
# preferencia de personas

import json
import csv
from datetime import datetime


# Cargar datos de restaurantes desde el archivo JSON
def cargar_restaurantes(file_path):
    with open(file_path, "r") as file:
        restaurantes = json.load(file)
    return restaurantes


# Cargar datos de viajeros desde el archivo CSV
def cargar_viajeros(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        viajeros = [row for row in reader]
    return viajeros


# Calcular la distancia entre dos puntos (coordenadas latitud y longitud)
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Implementa la fórmula para calcular la distancia entre dos puntos geográficos
    pass


# Filtrar restaurantes por proximidad
def filtrar_por_proximidad(restaurantes, viajero):
    # Calcula la distancia entre cada restaurante y el alojamiento del viajero
    # Filtra los restaurantes que están dentro de un radio determinado de la ubicación del viajero
    pass


# Filtrar restaurantes por horarios de apertura y cierre
def filtrar_por_horarios(restaurantes, fecha, hora):
    # Filtra los restaurantes que están abiertos en la fecha y hora especificadas
    pass


# Filtrar restaurantes por preferencias del viajero
def filtrar_por_preferencias(restaurantes, preferencias):
    # Filtra los restaurantes que coinciden con las preferencias del viajero
    pass


# Generar itinerario de restaurantes para un viajero
def generar_itinerario(viajero, restaurantes):
    itinerario = {}
    # Itera sobre los días de estancia del viajero
    for dia in range(viajero["dias_estancia"]):
        fecha = viajero["fecha_llegada"] + timedelta(days=dia)
        # Filtra los restaurantes disponibles en la fecha específica
        restaurantes_disponibles = filtrar_por_horarios(
            restaurantes, fecha, viajero["hora_disponible"]
        )
        # Filtra los restaurantes por proximidad al alojamiento del viajero
        restaurantes_proximos = filtrar_por_proximidad(
            restaurantes_disponibles, viajero
        )
        # Filtra los restaurantes por preferencias del viajero
        restaurantes_preferidos = filtrar_por_preferencias(
            restaurantes_proximos, viajero["preferencias"]
        )
        # Agrega los restaurantes al itinerario del día
        itinerario[fecha] = restaurantes_preferidos
    return itinerario


# Guardar el itinerario generado en un archivo CSV
def guardar_itinerario(itinerario, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Restaurantes"])
        for fecha, restaurantes in itinerario.items():
            writer.writerow([fecha, ", ".join(restaurantes)])


# Ejemplo de uso
def main():
    restaurantes = cargar_restaurantes("restaurantes.json")
    viajeros = cargar_viajeros("viajeros.csv")
    for viajero in viajeros:
        itinerario = generar_itinerario(viajero, restaurantes)
        guardar_itinerario(itinerario, f"itinerario_{viajero['id']}.csv")


if __name__ == "__main__":
    main()
