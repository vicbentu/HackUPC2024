import json

RESTAURANTS_JSON = "dataset/restaurants.json"


class Restaurants:
    def __init__(self):
        self.restaurants = json.load(open(RESTAURANTS_JSON))

    def getRestaurants(self):
        return self.restaurants

    def getRestaurantsInCity(self, city):
        return [
            restaurant["restaurant ID"]
            for restaurant in self.restaurants
            if restaurant["city"]["name"] == city
        ]
