from scheduler import Scheduler
from datetime import datetime

city = 'Berlin'
arrival_date = datetime(day=8, month=2, year=2024)
departure_date = datetime(day=30, month=3, year=2024)

myScheduler = Scheduler()
for e in myScheduler.getSchedule(city, arrival_date, departure_date):
    print(e)
