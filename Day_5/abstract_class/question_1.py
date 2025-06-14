from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def number_of_sides(self):
        return 0

class Quadilateral(Polygon):
    def number_of_sides(self):
        return 4
    
class Pentagon(Polygon):
    def number_of_sides(self):
        return 5
    
class Hexagon(Polygon):
    def number_of_sides(self):
        return 6
    
quad = Quadilateral()
pent = Pentagon()
hex = Hexagon()