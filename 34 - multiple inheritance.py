class A:
    def abc(self):
        print("Class A >> abc method")

class B(A):
    def abc(self):
        print("Class B >> abc method")

class C(A):
    def abc(self):
        print("Class C >> abc method")

class D(B,C):
    pass

d = D()
d.abc()