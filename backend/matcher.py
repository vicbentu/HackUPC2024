from datetime import *
import csv

class Matcher:
    def __init__(self):
        with open('dataset/hackupc-travelperk-dataset.csv', mode ='r') as file:    
            self.csvFile = list(csv.DictReader(file))
    def read(self):
        for lines in self.csvFile:
            print(lines)

    def getPotentialMatches(self, place, departureDate, returnDate):
        def intersects(d1, r1, d2, r2):
            return d1 <=r2 and d2 <= r2

        L = []
        for line in self.csvFile:
            depD = datetime.strptime(line['Departure Date'], '%d/%m/%Y')
            retD = datetime.strptime(line['Return Date'], '%d/%m/%Y')
            # depD = line['Departure Date']
            # retD = line['Return Date']
            plc = line['Arrival City']
            if place == plc and intersects(depD, retD, departureDate, returnDate):
                L.append(int(line['Trip ID']))
        return L
