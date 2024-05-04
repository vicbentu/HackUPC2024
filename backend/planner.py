from scheduler import Scheduler
from travelers import Travelers
from geopy.distance import geodesic
from datetime import datetime, timedelta
import random

MAXDISTANCE = 5


class Planner:
    def __init__(self):
        self.scheduler = Scheduler()
        self.travelers = Travelers()

    def plan_itinerary(self, city, arrival_date, departure_date, traveler_id):
        schedule = self.scheduler.getSchedule(city, arrival_date, departure_date)
        gustos = self.travelers.get_traveler_gustos(traveler_id)
        itinerary = []

        for item in schedule:
            date = item["date"]
            group = item["group"]
            restaurant = item["restaurant"]

            if restaurant:
                # Filtrar por proximidad
                print(group)
                print(restaurant)
                group = self.filtrar_por_proximidad(group, restaurant)

                # Filtrar por horarios de apertura y cierre
                group = self.filtrar_por_horarios(group, date)

                # Filtrar por los gustos de la persona
                group = self.filtrar_por_preferencias(group, gustos)

                # Agregar el restaurante seleccionado al itinerario
                itinerary.append({"date": date, "restaurant": restaurant})

        return itinerary

    def calculate_distance(self, restaurante1, restaurante2):
        # Supongamos que los restaurantes tienen atributos 'latitude' y 'longitude'
        coordenadas1 = (restaurante1["latitude"], restaurante1["longitude"])
        coordenadas2 = (restaurante2["latitude"], restaurante2["longitude"])
        distancia = geodesic(coordenadas1, coordenadas2).kilometers
        return distancia

    def filtrar_por_proximidad(self, group, restaurant):
        # Supongamos que la función calcular_distancia está definida en Matcher
        # y devuelve la distancia entre dos puntos geográficos
        for otro_restaurante in group:
            if self.calculate_distance(restaurant, otro_restaurante) < MAXDISTANCE:
                group.append(otro_restaurante)
        return group

    def filtrar_por_horarios(self, group, date):
        # Supongamos que los horarios de apertura y cierre están disponibles en cada restaurante
        horario_apertura = date.replace(
            hour=9, minute=0
        )  # Por ejemplo, abre a las 9:00 am
        horario_cierre = date.replace(
            hour=21, minute=0
        )  # Por ejemplo, cierra a las 9:00 pm
        group_filtrado = [
            restaurante
            for restaurante in group
            if horario_apertura <= restaurante["hora_apertura"] <= horario_cierre
        ]
        return group_filtrado

    def filtrar_por_preferencias(self, group, gustos_persona):
        group_filtrado = [
            restaurante
            for restaurante in group
            if any(gusto in restaurante["categorias"] for gusto in gustos_persona)
        ]
        return group_filtrado
