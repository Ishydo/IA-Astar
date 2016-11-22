from City import *
from tools import *
from f_heuristics import *
from State import *
import operator

# ASTAR CONFIGURATION #################################################
SOURCE_CITY = "Warsaw"      # Source city
TARGET_CITY = "Lisbon"      # Desination city
HEURISTIC_FUNCTION = h4     # Heuristic function
PRINT_STEPS_MODE = True     # Print frontiere + history each iteration
######################################################################

cities = []
cities_dict = {}

#Astar method
def astar_search(sourceCityState, targetCity):

    iterations = 0 # Pour les observations

    frontiere = [sourceCityState] # La première ville visitée. L'état de la source définie
    history = set() # On initialise un historique vide

    # Tant qu'il y a des villes à visiter dans frontière
    while frontiere:

        iterations += 1 # Une iteration en plus

        openstates = set()
        openstatesf = set()

        cityState = frontiere.pop() # On récupère le tout premier état

        if PRINT_STEPS_MODE:    # Debug mode
            print("frontiere = " + str(frontiere))
            print("history = " + str(history))

        if cityState.final(targetCity): # On retourne l'état actuel si sa ville est la cible
            history.add(cityState)      # On ajoute l'état visité à l'historique
            print("Successfully found !")
            print(" -> " + str(len(history)) + " visited cities.")
            print(" -> " + str(iterations) + " a* algorithm iterations.")

            print("-----------------------------------------")
            return cityState

        history.add(cityState)      # On ajoute l'état visité à l'historique

        possibleDestinations = cityState.possible_destinations() # Si la ville n'est pas trouvée on récupère les destinations possibles (voisins directs de la ville visitée)
        for possibleCity in possibleDestinations: # Pour chacune des destinations possibles, on crée un nouvel état
            newCityState = cityState.apply(possibleCity[1], HEURISTIC_FUNCTION(possibleCity[1], targetCity), possibleCity[0]) # Nouvel état avec la nouvelle ville à visiter, l'heuristique et la distance
            if (newCityState not in history) and newCityState.legal(): # Si cet état n'est pas dans l'historique alors on l'ajoute dans frontière
                frontiere.append(newCityState)

        # Finalement on trie la frontière en fonction de l'attribut f de l'état (f = h + g)
        frontiere = sorted(frontiere, key=operator.attrgetter('f'), reverse=True)

if __name__ == '__main__':

    load_cities(cities)         # Remplissage du tableau de ville (tools.py)
    load_connections(cities)    # Initialisation des connexions (tools.py)

    # Création d'un dictionnaire avec clé nom de la ville en string (pour facilité de récupération)
    for city in cities:
        cities_dict[city.name] = city

    # Récupération des villes source et cible selon confguration
    sourceCity = cities_dict[SOURCE_CITY]
    targetCity = cities_dict[TARGET_CITY]

    # Récupération du résultat avec a*
    astar_result = astar_search(State(sourceCity, HEURISTIC_FUNCTION(sourceCity, targetCity)), targetCity)

    # Affichage de la réponse avec chemin
    print_result(astar_result)
