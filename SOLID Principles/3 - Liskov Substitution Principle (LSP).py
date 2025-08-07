'''

Liskov Substitution Principle (LSP): 

Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. 
In other words, a subclass should be substitutable for its superclass without altering the desirable properties of the program.

'''


class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")
