from datetime import *

import csv


class Matcher:
    def __init__(self):
        with open("dataset/output.csv", mode="r") as file:
            self.file = list(csv.DictReader(file))

    def read(self):
        for lines in self.csvFile:
            print(lines)

    def getPotentialMatches(self, place, departureDate, returnDate):
        def intersects(d1, r1, d2, r2):
            return d1 <= r2 and d2 <= r2

        L = []
        for line in self.file:
            depD = datetime.strptime(line["Departure Date"], "%d/%m/%Y")
            retD = datetime.strptime(line["Return Date"], "%d/%m/%Y")
            # depD = line['Departure Date']
            # retD = line['Return Date']
            plc = line["Arrival City"]
            if place == plc and intersects(depD, retD, departureDate, returnDate):
                L.append(int(line["Trip ID"]))
        return L

    def getCities(self):
        L = []
        for x in self.file:
            if x["Arrival City"] not in L:
                L.append(x["Arrival City"])
        return L

    def exactMatch(self, matches, city, date):
        def betweenDate(self, id):
            depD = datetime.strptime(self.file[id - 1]["Departure Date"], "%d/%m/%Y")
            retD = datetime.strptime(self.file[id - 1]["Return Date"], "%d/%m/%Y")
            return depD <= date and retD >= date

        return [
            self.file[id - 1]["Traveller Name"]
            for id in matches
            if self.file[id - 1]["Arrival City"] == city and betweenDate(self, id)
        ]

    def filtrar_por_proximidad(self, group, restaurant):
        # Implementa la lógica para filtrar por proximidad utilizando la función calculate_distance
        pass

    def filtrar_por_horarios(self, group, date):
        # Implementa la lógica para filtrar por horarios de apertura y cierre
        pass

    def filtrar_por_preferencias(self, group, gustos_persona):
        # Implementa la lógica para filtrar por los gustos de la persona
        pass
