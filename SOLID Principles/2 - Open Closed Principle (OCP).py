'''

Open/Closed Principle (OCP): 

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. 
This means that you should be able to extend the behavior of a module without modifying its source code.

'''


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
