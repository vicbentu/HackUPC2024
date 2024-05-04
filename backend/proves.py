from planner import Planner  # Asegúrate de que esta es la clase correcta
from datetime import datetime

city = "Barcelona"
arrival_date = datetime(day=7, month=9, year=2024)
departure_date = datetime(day=20, month=9, year=2024)


myPlanner = Planner()  # Crea una instancia de la clase Planner
schedule = myPlanner.plan_itinerary(
    city, arrival_date, departure_date, 7
)  # Llama al método getSchedule


for e in schedule:
    print(e)
