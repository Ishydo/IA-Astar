# A-Star search algorithm python implementation

A little implementation of AStar search algorithm in python with a few defined
basic heurisitc functions. Still a lot of improvements to do.

## Execution modes & configuration

Execution behaviour can be changed in TP_Astar.py with a few parameters.

```python
# ASTAR CONFIGURATION #################################################
SOURCE_CITY = "Warsaw"      # Source city
TARGET_CITY = "Lisbon"      # Desination city
TEST_ALL_HEURISTIC = True   # Choisir si exécute toutes les heuristiques ou celle d'en dessous
HEURISTIC_FUNCTION = h4     # Heuristic function [h0, h1, h2, h3, h4]
PRINT_STEPS_MODE = True     # Print frontiere + history each iteration
######################################################################
```

## Heuristic functions

Can be added / modified in f_heuristics.py.

```python
def h0(cityA, cityB):
    return 0

def h1(cityA, cityB):
    return fabs(cityA.x - cityB.x)

def h2(cityA, cityB):
    return fabs(cityA.y - cityB.y)

def h3(cityA, cityB):
    return cityA.distance_bird(cityB)

def h4(cityA, cityB):
    return h1(cityA, cityB) + h2(cityA, cityB)
```
