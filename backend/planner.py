# from scheduler import Scheduler
# from travelers import Travelers
# from geopy.distance import geodesic
# from datetime import datetime, timedelta
# from restaurants import Restaurants
# import random
# import json

# MAXDISTANCE = 5
# RESTAURANTS_JSON = "dataset/restaurants.json"


# class Planner:
#     def __init__(self):
#         self.scheduler = Scheduler()
#         self.travelers = Travelers()
#         self.restaurants = json.load(open(RESTAURANTS_JSON))

#     def plan_itinerary(self, city, arrival_date, departure_date, traveler_id):
#         schedule = self.scheduler.getSchedule(city, arrival_date, departure_date)
#         itinerary = []

#         for item in schedule:
#         item = schedule
#             print(item)
#             city = self.restaurants[item["restaurant"]]["city"]
#             print(city)
#             date = item["date"]
#             group = item["group"]
#             restaurant = item["restaurant"]
#             caca = Restaurants()
#             restaurants = caca.getRestaurantsInCity(city)
#             for rest in restaurants:
                
        

#             # if restaurant:
#             #     # Filtrar por proximidad
#             #     print(group)
#             #     print(restaurant)

#             #     # Filtrar por los gustos de la persona
#             #     group = self.filtrar_por_preferencias(restaurant, group)

                
#             #     # Filtrar por horarios de apertura y cierre
#             #     group = self.filtrar_por_horarios(group, date)

#             #     # Agregar el restaurante seleccionado al itinerario
#             #     itinerary.append({"date": date, "restaurant": restaurant})

#         return itinerary

   

#     def filtrar_por_horarios(self, group, date):
#         # Supongamos que los horarios de apertura y cierre están disponibles en cada restaurante
#         horario_apertura = date.replace(
#             hour=9, minute=0
#         )  # Por ejemplo, abre a las 9:00 am
#         horario_cierre = date.replace(
#             hour=21, minute=0
#         )  # Por ejemplo, cierra a las 9:00 pm
#         group_filtrado = [
#             restaurante
#             for restaurante in group
#             if horario_apertura <= restaurante["hora_apertura"] <= horario_cierre
#         ]
#         return group_filtrado

#     def filtrar_por_preferencias(self, restaurant, group):
#         rest_types = self.restaurants[restaurant][category]
#         group_filtrado = [
#             # restaurante
#             # for restaurante in group
#             # if any(gusto in restaurante["categorias"] for gusto in gustos_persona)
            
#         ]
#         return group_filtrado
