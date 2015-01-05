class City(object):
    def __init__(self, index, name, x, y, distances):
        self.index = index
        self.name = name
        self.x = x
        self.y = y
        self.distances = distances
    
    def getIndex(self): return self.index
    
    def getName(self): return self.name
        
    def getX(self): return self.x
    
    def getY(self): return self.y
    
    def getDistances(self): return self.distances
    
    def getDistanceTo(self, index): return self.distances[index]