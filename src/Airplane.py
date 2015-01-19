class Airplane(object):
    MAX_PASSENGERS = 199
    MAX_DISTANCE = 3199
    AIRPLANE_SPEED = 800        # km/h
    MAX_NUMBER_OF_FLIGHTS = 20
    MINUTES_PER_DAY = 1200
    
    def __init__(self, index, homebase, startCity, color):
        self.index = index
        self.homebase = homebase
        self.numberOfFlights = 0
        self.distanceCovered = 0
        self.startCity = startCity
        self.currentCity = startCity
        self.color = color
        self.route = [0 for x in range(self.MAX_NUMBER_OF_FLIGHTS)]
        self.passengerKilometer = 0
        
    def __copy__(self): return type(self)    
    
    def getIndex(self): return self.index
    
    def getMaxPassengers(self): return self.MAX_PASSENGERS
    
    def getAirplanePoints(self): return self.passengerKilometer
    
    def getMaxDistance(self): return self.MAX_DISTANCE
    
    def getAirplaneSpeed(self): return self.AIRPLANE_SPEED
    
    def getHomebase(self): return self.homebase
    
    def getColor(self): return self.color
    
    def setCurrentCity(self, city): self.currentCity = city
    
    def getCurrentCity(self): return self.currentCity
    
    def getStartCity(self): return self.startCity
    
    def addFlight(self, flight):
        if(flight.getNumberOfPassengers() > self.MAX_PASSENGERS):
            print "Only 199 passengers fit in the Airplane from", flight.getDepartureCity().getName(), "to", flight.getArrivalCity().getName() 
            quit()
        elif(self.isValid(flight.getArrivalCity())):
            self.route[self.numberOfFlights] = flight
            self.numberOfFlights += 1
            self.currentCity = flight.getArrivalCity()
            if(flight.getsRefueled()): self.distanceCovered = 0
            else: self.distanceCovered += flight.getFlightDistance()
            self.passengerKilometer += flight.getFlightPoints()
        
    def removeLastFlight(self):
        self.numberOfFlights -= 1
        
    def getFlight(self, index): 
        if(index < self.numberOfFlights):
            return self.route[index]
        else: 
            return False
        
    def getNumberOfFlights(self): return self.numberOfFlights
    
    def homebaseVisited(self):
        for flight in self.route:
            if(flight.getDepartureCity.getName() == self.homebase or
               flight.getArrivalCity.getName() == self.homebase):
                return True
        return False
    
    def isValid(self, city):
        distance = self.currentCity.getDistanceTo(city.getIndex())
        flightTime = (distance / self.AIRPLANE_SPEED) * 60
        time = 0
        for i in range(self.numberOfFlights):
            time += self.route[i].getTotalTimeFlight()
                
        if(distance < (self.MAX_DISTANCE - self.distanceCovered)):
            if(flightTime < (self.MINUTES_PER_DAY - time)):
               return True
            #else: print "Cannot fly to", city.getName(), ", will not arrive before 02:00."
        else: print "Cannot fly to", city.getName(), ", needs refueling in", self.currentCity.getName()
        return False
