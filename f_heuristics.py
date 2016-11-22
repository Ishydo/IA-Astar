from City import *
from math import fabs

def h0(cityA, cityB):
    return 0

def h1(cityA, cityB):
    return fabs(cityA.x - cityB.y)

def h2(cityA, cityB):
    return fabs(cityA.x - cityB.y)

def h3(cityA, cityB):
    return cityA.distance_bird(cityB)

def h4(cityA, cityB):
    return h1(cityA, cityB) + h2(cityA, cityB)
