from Tkinter import *
from PIL import ImageTk

class TrafficFrame(object):
    def __init__(self, traffic):
        self.root = Tk()
        self.traffic = traffic
        
        self.frame = Frame(self.root, width=1024, height=768, colormap="new")
        self.frame.pack(fill=BOTH,expand=1)
        
        self.label = Label(self.frame, text="Heuristieken 2015 - Mokum Airways!")
        self.label.pack(fill=X, expand=1)
        
        self.canvas = Canvas(self.frame, 
                             bg="white", 
                             width=701, 
                             height=599)
        
        self.image = ImageTk.PhotoImage(file = "../resources/europe-scaled.png")
        self.canvas.create_image(0, 0, image = self.image, anchor = NW)   
        
        self.canvas.bind("<Button-1>", self.processMouseEvent)
        self.canvas.focus_set()
        
        self.text = Text(self.root, bd=4, width=100, height=6)
    
    def setCities(self, cities):
        for city in cities:
            x = city.getX()
            y = city.getY()
            self.canvas.create_rectangle(x-2, y-2, x+2, y+2, fill = "Black")
            self.canvas.create_text(x, y+5, text = city.getName())
            
    def showDistance(self, city1, city2, color="Black"):
        self.canvas.create_line(city1.getX(), city1.getY(), city2.getX(), city2.getY(), arrow="last", fill=color, width=2)
        self.canvas.create_text((city1.getX() + city2.getX()) / 2,
                                (city1.getY() + city2.getY()) / 2,
                                text = city1.getDistanceTo(city2.getIndex()))
    
    def showAllDistances(self, cities):
        for city1 in cities:
            for city2 in cities:
                if(city1 != city2): self.showDistance(city1, city2)
            
    def setTraffic(self):
        for airplane in self.traffic.traffic:
            self.text.insert(INSERT, "Airplane ")
            self.text.insert(INSERT, airplane.getIndex() + 1)
            self.text.insert(INSERT, " (")
            self.text.insert(INSERT, airplane.getAirplanePoints())
            self.text.insert(INSERT, "): " +
                                     airplane.getStartCity().getName() +
                                     "[")
            for i in range(airplane.getNumberOfFlights()):
                flight = self.traffic.traffic[airplane.getIndex()].getFlight(i)
                self.text.insert(INSERT, flight.getDepartureTime())
                self.text.insert(INSERT, "]-[")
                self.text.insert(INSERT, flight.getArrivalTime())
                self.text.insert(INSERT, "]" +
                                         flight.getArrivalCity().getName() +
                                         "[")
                self.showDistance(flight.getDepartureCity(), flight.getArrivalCity(), self.traffic.traffic[airplane.getIndex()].getColor())
            self.text.insert(INSERT, "\n")
        
        self.canvas.pack()
        self.text.pack(fill=BOTH, expand=1)

    def run(self):
        self.root.after(10,self.repaint)
        self.root.mainloop()
        

    def repaint(self):
        self.text.delete(1.0, END)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image = self.image, anchor = NW)   
        self.traffic.setAirplanes()
        cities = self.traffic.distanceMap.getCities()
        self.setCities(cities)
        self.setTraffic()
        self.root.after(10,self.repaint)
            
    def processMouseEvent(self, event):
        coordinates = ((event.x), ",", (event.y))
        self.canvas.create_text(event.x, event.y, text = coordinates)
