class Flight(object):
    DOCKING_TIME = 60
    REFUEL_TIME = 60
    
    def __init__(self, passengers, departurTime, departureCity, arrivalTime, arrivalCity, distance, refuel):
        self.passengers = passengers
        self.departurTime = departurTime
        self.departureCity = departureCity
        self.arrivalTime = arrivalTime
        self.arrivalCity = arrivalCity
        self.distance = distance
        self.processTime = self.DOCKING_TIME
        self.refuel = False
        if(refuel): self.setRefuel()
        self.waitingTime = 0
    
    def getNumberOfPassengers(self): return self.passengers
    
    def setNumberOfPassengers(self, passengers): self.passengers = passengers
    
    def getArrivalCity(self): return self.arrivalCity
    
    def getDepartureCity(self): return self.departureCity
    
    def getFlightDistance(self): return self.distance
    
    def getDepartureTime(self): return self.departurTime
    
    def getArrivalTime(self): return self.arrivalTime
    
    def getTravelTime(self): return self.arrivalTime - self.departurTime
    
    def getProcessTime(self): return self.processTime
        
    def getWaitingTime(self): return self.waitingTime
    
    def wait(self, time): self.waitingtime += time
    
    def removeWaitingTime(self): self.waitingTime = 0
    
    def getGroundTime(self): return self.getProcessTime() + self.getWaitingTime()
    
    def getTotalTimeFlight(self): return self.getGroundTime() + self.getTravelTime()
            
    def setRefuel(self):
        if(not self.refuel):
            self.refuel = True
            self.processTime += self.REFUEL_TIME
    
    def removeRefuel(self):
        if(self.refuel):
            self.refuel = False
            self.processTime -= self.REFUEL_TIME
    
    def getsRefueled(self): return self.refuel
    
    def getFlightPoints(self): return self.passengers * self.distance