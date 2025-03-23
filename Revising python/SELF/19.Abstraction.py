###################### It is mandatory to Import abc module, ABC class , abstractmethod ######################
### abc -> Abstract Base Class ###
### Works as template for child class ###
### we cant create object of abstract class ###

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14*self.radius**2
        print(f"Area of Circle is {area}")
    
    def perimeter(self):
        peri = 2*3.14*self.radius
        print(f"perimeter of circle is {peri}")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length*self.breadth
        print(f"Area of reactangle is {area}")
    
    def perimeter(self):
        peri = (2*self.length)+(2*self.breadth)
        print(f"perimeter of Rectangle is {peri}")

circle = Circle(5)
circle.area()
circle.perimeter()

rect = Rectangle(3,5)
rect.area()
rect.perimeter()

        
