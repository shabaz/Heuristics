import random

from DistanceMap import DistanceMap
from Airplane import Airplane
from Flight import Flight

def check_feasible(tour):
    total_distance = 0
    prev_city = tour[0]


    time_refueling = 0 # TODO
    tank_capacity_in_kms = Airplane.MAX_DISTANCE

    for i in tour[1:]:
        next_distance = DistanceMap.DISTANCES[prev_city][i]
        if next_distance > Airplane.MAX_DISTANCE:
            return False
        if next_distance > tank_capacity_in_kms:
            time_refueling += Flight.REFUEL_TIME
            tank_capacity_in_kms = Airplane.MAX_DISTANCE
        total_distance += next_distance
        tank_capacity_in_kms -= next_distance
        prev_city = i

    time_in_air = float(total_distance) / Airplane.AIRPLANE_SPEED * 60.0
    time_docking = (len(tour)-1) * Flight.DOCKING_TIME


    return time_in_air + time_docking + time_refueling <= Airplane.MINUTES_PER_DAY


def create_subtour(start_tour, end_tour):
    start_node = start_tour[-1]
    end_node = end_tour[0]

    new_subtour = []

    while True:
        feasible_next_cities = []
        for i in xrange(28):
            if i == start_node:
                continue

            if check_feasible(start_tour + new_subtour + [i] + end_tour):
                feasible_next_cities.append(i)

        if (feasible_next_cities):
            next_city = random.choice(feasible_next_cities)
            new_subtour.append(next_city)
            start_node = next_city
        else:
            return start_tour + new_subtour + end_tour
            break


