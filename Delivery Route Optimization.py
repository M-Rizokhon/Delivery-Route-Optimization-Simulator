# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:12:40 2025

@author: Muhammad Rizo
"""
import random

class Location(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def getName(self):
        return self.name
    def distFrom(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    

class Truck(object):
    def __init__(self, id_number, capacity):
        self.id_number = id_number
        self.cap = capacity
    def getID(self):
        return self.id_number
    def getCapacity(self):
        return self.cap


def nearestNeighbor(start, locs, truck):
    route = [start]
    current_location = start
    remaining = locs[:]
    while remaining and len(route) <= truck.getCapacity():
        nearest = min(remaining, key = lambda loc : loc.distFrom(current_location))
        route.append(nearest)
        remaining.remove(nearest)
        current_location = nearest
        
    route.append(start)
    return route

def totalDistance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += route[i].distFrom(route[i+1])
    return total_distance


def assignTrucks(locs, warehouse, trucks):
    random.shuffle(locs)
    routes = []
    remaining = locs[:]
    
    for i in range(len(trucks)):
        if not remaining:
            break
        route = nearestNeighbor(warehouse, remaining, trucks[i])
        routes.append(route)
        
        visited = set(route)
        remaining = [loc for loc in remaining if loc not in visited]
        
    for i in range(len(routes)):
        print('Truck ', trucks[i].getID())
        for loc in routes[i]:
            print(loc.getName() + ' -> ', end='')
        print('end\n')
    
    total_distance = 0
    for route in routes:
        total_distance += totalDistance(route)
    print('Total distance traveled', round(total_distance, 2), 'km')




truck1 = Truck('101', 3)
truck2 = Truck('102', 5)
truck3 = Truck('103', 4)
trucks = [truck1, truck2, truck3]
warehouse = Location('Warehouse', 0, 0)
locs = [
        Location('KFC', 4, 10),
        Location("Wendy's", 8, 4),
        Location('Pizza hut', 18, 3),
        Location('Burger king', 17, 10),
        Location("McDonald's", 10, 9),  
        Location("Little italy", 20, 56),
        Location("In-n-out", 34, 45),
        Location('Evos', 27, 35),
        Location('Dominos', 40, 50)
        ]


assignTrucks(locs, warehouse, trucks)



















































