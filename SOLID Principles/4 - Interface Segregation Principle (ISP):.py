'''

Interface Segregation Principle (ISP): 

Clients should not be forced to depend on interfaces they don't use. 
This principle suggests that interfaces should be specific to the needs of the clients, avoiding the "fat" or overly generalized interfaces.

'''
class Worker:
    def work(self):
        pass

class Manager(Worker):
    def work(self):
        print("Manager is managing")

class Developer(Worker):
    def work(self):
        print("Developer is coding")

class Tester(Worker):
    def work(self):
        print("Tester is testing")
