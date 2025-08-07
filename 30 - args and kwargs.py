# *args Python Example
def sum(*args):
    total = 0
    for a in args:
        total = total + a
        print(total)
sum(1,2,3,4,5)

# **Kwargs Python Example
def show(**kwargs):
    print(kwargs)

show(A=1,B=2,C=3)