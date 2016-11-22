from City import *

def print_result(astar_result):
    if astar_result is None:
        print("Aucun résultat trouvé !")
    else:
        pathToRoot = []
        distTot = 0
        while astar_result.parent is not None:
            pathToRoot.insert(0, astar_result)
            astar_result = astar_result.parent
        pathToRoot.insert(0, astar_result) # La ville racine

        for cityState in pathToRoot:
            distTot += cityState.distance
            print(cityState.city.name + " -> " + str(distTot))

# Loading connections between cities
def load_connections(cities):
    print("Loading connections from file.")
    with open('./connections.txt', 'r') as outfile:
        for line in outfile:
                splitted = line.split(" ")
                citySource = None
                cityDest = None
                for city in cities:
                    if city.name == splitted[0]:
                        citySource = city
                    elif city.name == splitted[1]:
                        cityDest = city
                dist = int(splitted[2])
                citySource.add_neighbour(cityDest, dist) # Ajout des connexions dans les deux sens
                cityDest.add_neighbour(citySource, dist)

# Loading positions of cities
def load_cities(cities):
    print("Loading distances from file.")
    positions = []
    with open('./positions.txt', 'r') as outfile:
        id = 0
        for line in outfile:
                splitted = line.rstrip('\n').split(" ")
                x = int(splitted[1])
                y = int(splitted[2])
                cities.append(City(id, splitted[0], x, y))  # Ajout de la ville à la liste
                id += 1
