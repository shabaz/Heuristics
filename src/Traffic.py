from DistanceMap import DistanceMap
#from TrafficFrame import TrafficFrame
from Airplane import Airplane
from Flight import Flight
from random import randint, randrange, random
import math
import copy

from createSubtour import create_subtour
from newsubtourgen import *



def choose_transition(new_points, prev_points, temperature):
    if new_points > prev_points:
        return True
    else:
        #new_points = 1.0/(new_points+1)
        #prev_points = 1.0/(prev_points+1)
        new_points /= 50
        prev_points /= 50
        transition_probability = math.exp((new_points - prev_points)/temperature)
        return random.random() < transition_probability
        

class Traffic(object):
    NUMBER_OF_AIRPLANES = 1
    
    PASSENGERS = [[0,213,119,278,89,302,388,153,341,273,112,361,302,324,269,206,147,400,367,172,45,321,100,135,86,95,257,371],
                  [373,0,377,341,202,161,354,182,424,69,96,52,141,5,224,425,277,88,380,290,444,89,0,28,376,296,323,7],
                  [403,165,0,327,231,403,113,287,218,264,443,166,436,322,37,206,252,291,414,271,223,287,408,251,127,299,3,58],
                  [143,238,15,0,110,380,387,205,280,65,208,56,289,82,221,249,273,363,77,272,365,444,175,363,35,428,206,61],
                  [320,360,375,345,0,433,246,239,82,20,205,350,271,41,335,327,31,307,17,262,424,349,273,369,253,448,238,263],
                  [86,1,281,370,75,0,354,255,22,31,105,342,183,73,120,91,256,89,70,236,108,242,274,421,331,166,329,249],
                  [49,264,371,277,292,3,0,330,363,143,197,184,209,50,414,164,421,394,262,390,214,363,28,187,337,187,96,34],
                  [110,413,36,366,31,174,75,0,102,138,101,269,283,205,166,38,38,332,118,352,59,338,14,91,332,20,418,163],
                  [46,313,371,24,87,414,44,196,0,49,78,351,112,432,290,121,369,5,187,97,55,428,41,264,441,191,37,245],
                  [119,262,389,175,147,431,194,368,319,0,62,107,85,120,129,96,342,302,425,245,187,419,189,133,315,424,289,92],
                  [261,20,14,81,390,154,41,450,356,165,0,75,291,41,55,138,58,88,350,295,84,150,334,120,101,405,280,65],
                  [244,362,175,118,38,201,332,168,417,324,162,0,363,137,4,170,232,326,397,302,3,5,4,359,347,369,413,308],
                  [251,248,431,243,318,398,407,290,378,45,70,16,0,140,94,100,215,293,265,202,168,374,51,293,120,435,368,324],
                  [91,424,232,148,310,410,120,393,406,266,110,434,450,0,193,288,40,128,442,144,63,95,9,341,110,220,320,138],
                  [235,136,341,383,255,414,181,228,223,140,76,304,326,293,0,438,23,93,123,378,449,362,203,194,386,123,365,373],
                  [191,359,76,10,39,293,116,129,4,314,428,273,388,342,321,0,18,239,402,164,441,47,429,423,9,276,334,323],
                  [179,430,128,330,307,405,87,202,91,325,91,209,42,309,446,434,0,280,415,106,333,161,309,403,383,430,117,246],
                  [5,360,144,212,46,48,409,375,267,326,51,306,95,16,365,59,8,0,351,37,219,397,242,245,245,407,30,375],
                  [25,61,232,425,309,252,38,69,205,77,310,350,328,393,177,106,21,102,0,219,56,126,318,265,120,247,263,426],
                  [79,103,351,40,133,150,116,0,206,187,369,157,295,177,115,152,331,366,154,0,4,122,402,342,379,361,382,325],
                  [206,25,450,341,234,100,345,290,179,81,388,285,415,222,83,280,227,352,181,440,0,81,378,331,100,113,304,109],
                  [316,4,398,268,419,161,73,36,96,385,373,434,123,295,16,172,109,360,196,356,263,0,382,314,322,352,120,417],
                  [157,62,337,246,314,271,250,180,387,386,379,41,255,49,139,332,283,313,337,7,121,97,0,275,357,348,78,413],
                  [107,403,353,383,54,407,142,66,360,408,377,80,430,193,131,341,216,176,224,77,251,43,381,0,16,122,175,237],
                  [285,335,166,287,215,108,275,131,362,267,250,18,421,302,280,57,368,100,391,390,134,391,77,409,0,157,244,100],
                  [373,433,407,186,98,377,122,110,247,398,299,236,12,15,78,177,307,260,135,27,272,288,127,153,415,0,257,324],
                  [312,322,57,159,135,450,15,12,92,47,41,440,315,39,193,124,224,68,439,28,290,287,366,153,427,115,0,314],
                  [441,256,62,423,215,432,412,128,361,128,138,360,87,181,113,389,200,141,300,281,337,9,180,203,379,290,165,0]]
    
    COLOR = ["Cyan", "BLUE", "GREEN", "RED", "YELLOW", "MAGENTA"]
    
    def __init__(self):
        self.currentTime = 0.0
        self.passengers = copy.deepcopy(self.PASSENGERS)
        self.distanceMap = DistanceMap()
        self.cities = self.distanceMap.getCities()
        self.traffic = self.setAirplanes()
        #self.frame = TrafficFrame(self.traffic)
        #self.frame.setCities(self.cities)
        #self.frame.setTraffic()
        
    def setAirplanes(self):
        #an example of a flight plan
        #try to change values to create a frame


        best_traffic = None
        best_score = 0
        best_passengers = None
        best_current_time = None
        prev_tour = None

        f = open("score_over_time.dat", "w")
        
        temperature = 50000
       
        for m in xrange(10000):

            traffic = [0 for x in range(self.NUMBER_OF_AIRPLANES)]
            for i in range(len(traffic)):
                traffic[i] = Airplane(i, self.cities[0], self.cities[0], self.COLOR[i])

                if not prev_tour:
                    tour = gen_tour()
                else:
                    tour = permutate_tour(prev_tour)
                #tour = [0, 25, 20, 6, 27, 16, 11]
                #tour = [0, 26, 14, 22, 13, 24]
                #tour = [0, 1, 15, 25, 21]

                prev_city = self.cities[tour[0]]
                prev_flight = None
                for j in tour[1:]+[tour[0]]:
                    next_city = self.cities[j]

                    flight_distance = prev_city.getDistanceTo(next_city.getIndex())
                    if flight_distance + traffic[i].distanceCovered >= Airplane.MAX_DISTANCE:
                        prev_flight.setRefuel()
                        traffic[i].distanceCovered = 0 # fill the tank of plane 

                    passengers =  min(self.passengers[prev_city.getIndex()][j], 199)

                    flight = Flight(passengers,
                            self.currentTime, 
                            prev_city, 
                            (float(prev_city.getDistanceTo(next_city.getIndex())) / traffic[i].getAirplaneSpeed() * 60) + self.currentTime, 
                            next_city, 
                            prev_city.getDistanceTo(next_city.getIndex()), 
                            False)
                    self.updatePassengerTable(prev_city, next_city, passengers)
                    self.currentTime += flight.getTotalTimeFlight()
                    traffic[i].addFlight(flight)
                    prev_city = next_city
                    prev_flight = flight
                    #print "traffic point", traffic[i].getAirplanePoints()

            traffic_points = 0
            for airplane in traffic:
                traffic_points += airplane.getAirplanePoints()

            if choose_transition(traffic_points, best_score, temperature):
            #if traffic_points > best_score:
                print tour
                print "new best score:", traffic_points
                print "temperature:", temperature
                #debug code
                if traffic_points == 0:
                    print tour
                    print m
                    quit()
                best_score = traffic_points
                best_traffic = traffic
                best_passengers = self.passengers
                best_current_time = self.currentTime
                prev_tour = tour
            self.passengers = copy.deepcopy(self.PASSENGERS)
            self.currentTime = 0.0

            f.write(str(m) + " " + str(best_score) + "\n")

            temperature *= 0.999


        self.passengers = best_passengers
        self.currentTime = best_current_time
        f.close()
        return best_traffic
    
    def updatePassengerTable(self, city1, city2, numberOfPassengers):
        if(self.passengers[city1.getIndex()][city2.getIndex()] < numberOfPassengers):
            print "There are only", self.passengers[city1.getIndex()][city2.getIndex()], "passengers who want to fly from", city1.getName(), "to", city2.getName()
            quit()
        else: self.passengers[city1.getIndex()][city2.getIndex()] -= numberOfPassengers
        

Traffic()
