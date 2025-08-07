from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):  # Abstract method
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Manadatory to implement this in child class
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Manadatory to implement this in child class
    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())

circle = Circle(3)
print("Area of Circle:", circle.area())
