class State:
    def __init__(self, city, h, g=0, distance=0, parent=None):
        self.city = city
        self.g = g
        self.f = g+h
        self.distance = distance
        self.parent = parent

    def legal(self):
        return True

    def final(self, final_city):
        return self.city == final_city

    def __hash__(self):
        return str(self).__hash__()

    def __str__(self):
        return str(self.city)

    def __eq__(self, other):
        return self.city.name == other.city.name

    def __repr__(self):
        return "["+self.city.name+"]"

    def possible_destinations(self):
        destinations = []
        # Retourne toutes les destinations possibles en fonction des voisins de la ville
        for connection in self.city.neighbours:
            destinations.append((connection[1], connection[0]))
        return destinations

    def apply(self, possibleCity, heuristic, dist):
        return State(possibleCity, heuristic, self.g+dist, dist, self) # On crée un nouvel état de ville avec la nouvelle distance de coût
