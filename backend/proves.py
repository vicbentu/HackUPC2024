from planner import Planner  # Asegúrate de que esta es la clase correcta
from datetime import datetime

city = "Berlin"
arrival_date = datetime(day=11, month=1, year=2024)
departure_date = datetime(day=14, month=1, year=2024)

myPlanner = Planner()  # Crea una instancia de la clase Planner
schedule = myPlanner.plan_itinerary(
    city, arrival_date, departure_date, 8
)  # Llama al método getSchedule


for e in schedule:
    print(e)
