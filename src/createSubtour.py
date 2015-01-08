import random

from DistanceMap import DistanceMap
from Airplane import Airplane
from Flight import Flight

def check_feasible(tour):
    total_distance = 0
    prev_city = tour[0]

    for i in tour[1:]:
        total_distance += DistanceMap.DISTANCES[prev_city][i]
        prev_city = i

    time_in_air = float(total_distance) / Airplane.AIRPLANE_SPEED * 60.0
    time_docking = (len(tour)-1) * Flight.DOCKING_TIME
    time_refueling = 0 # TODO


    return time_in_air + time_docking <= Airplane.MINUTES_PER_DAY


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
            print start_tour + new_subtour + end_tour
            break

create_subtour([0], [0])
