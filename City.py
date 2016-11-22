import math

class City:
    def __init__(self, _id, _name, _x, _y):
        self.id = _id
        self.name = _name
        self.x = _x
        self.y = _y
        self.neighbours = [] # Les connections, voisins directs de la ville selon fichier fourni

    def add_neighbour(self, target_city, distance):
        self.neighbours.append((target_city, distance))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def distance_x(self, otherCity):
        return math.fabs(self.x - otherCity.x)

    def distance_y(self, otherCity):
        return math.fabs(self.y - otherCity.y)

    def distance_bird(self, otherCity):
        return math.sqrt(math.pow(self.distance_x(otherCity), 2)+math.pow(self.distance_y(otherCity), 2))
