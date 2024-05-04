import csv

csv_file = "./dataset/output.csv"


class Travelers:
    def __init__(self):
        self.travelers_data = self.read_travelers_csv(csv_file)

    def read_travelers_csv(self, csv_file):
        travelers_data = {}
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                traveler_id = row["Trip ID"]
                gustos = row["favorite_categories"].split(",")
                travelers_data[traveler_id] = gustos
        return travelers_data

    def get_traveler_gustos(self, traveler_id):
        return self.travelers_data.get(traveler_id, [])


# Ejemplo de uso
if __name__ == "__main__":
    travelers = Travelers()
    traveler_id = "18"  # Cambia esto por el ID del viajero que quieras consultar
    gustos = travelers.get_traveler_gustos(traveler_id)
    print(f"Gustos del viajero {traveler_id}: {gustos}")
