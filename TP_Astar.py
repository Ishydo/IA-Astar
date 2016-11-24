from City import *
from tools import *
from f_heuristics import *
from State import *
import operator

# ASTAR CONFIGURATION #################################################
SOURCE_CITY = "Warsaw"      # Source city
TARGET_CITY = "Lisbon"      # Desination city
TEST_ALL_HEURISTIC = True   # Choisir si exécute toutes les heuristiques ou celle d'en dessous
HEURISTIC_FUNCTION = h4     # Heuristic function [h0, h1, h2, h3, h4]
PRINT_STEPS_MODE = True     # Print frontiere + history each iteration
######################################################################

cities = []
cities_dict = {}

#Astar method
def astar_search(sourceCityState, targetCity, h_func):

    iterations = 0 # Pour les observations

    frontiere = [sourceCityState] # La première ville visitée. L'état de la source définie
    history = set() # On initialise un historique vide

    # Tant qu'il y a des villes à visiter dans frontière
    while frontiere:

        iterations += 1 # Une iteration en plus

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
            newCityState = cityState.apply(possibleCity[1], h_func(possibleCity[1], targetCity), possibleCity[0]) # Nouvel état avec la nouvelle ville à visiter, l'heuristique et la distance
            if (newCityState not in history) and newCityState.legal(): # Si cet état n'est pas dans l'historique alors on l'ajoute dans frontière

                # Pour éviter les doublons dans la frontière
                present = False
                for regState in frontiere:
                    if regState.city.name == newCityState.city.name:
                        present = True
                        if newCityState.f < regState.f:
                            frontiere.remove(regState)
                            frontiere.append(newCityState)
                if(not present):
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

    funcDict = {0: h0, 1: h1, 2:h2, 3:h3, 4:h4}

    if TEST_ALL_HEURISTIC:
        for k, hfunc in funcDict.items():
            print("--------------------------------------------")
            print("------------- Execution en h" + str(k) + " --------------")
            print("--------------------------------------------")

            # Récupération du résultat avec a*
            astar_result = astar_search(State(sourceCity, hfunc(sourceCity, targetCity)), targetCity, hfunc)

            # Affichage de la réponse avec chemin
            print_result(astar_result)
    else: # N'exécute qu'avec l'heuristique définie
        # Récupération du résultat avec a*
        astar_result = astar_search(State(sourceCity, HEURISTIC_FUNCTION(sourceCity, targetCity)), targetCity, HEURISTIC_FUNCTION)

        # Affichage de la réponse avec chemin
        print_result(astar_result)
