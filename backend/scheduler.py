from matcher import Matcher
from restaurants import Restaurants
from datetime import datetime, timedelta
import random

class Scheduler:
    def __init__(self):
        self.restaurants = Restaurants()
        self.matcher = Matcher()
    
    def getSchedule(self, city, arrival_date, departure_date):
        matches = self.matcher.getPotentialMatches(city, arrival_date, departure_date)
        print(matches)
        restaurants_list = self.restaurants.getRestaurantsInCity(city)
        for restaurant in restaurants_list: print(restaurant)

        td = timedelta(days=1)
        date = arrival_date
        ret = []
        while date <= departure_date:
            group_count = random.randint(1, 3)
            matches_day = self.matcher.exactMatch(matches, city, date)
            group = random.sample(k=min(group_count, len(matches_day)), population=matches_day)
            restaurant = random.choice(self.restaurants.getRestaurantsInCity(city))
            ret.append({
                'date': date,
                'group': group,
                'restaurant': restaurant
            })
            date += td
        return ret
            

