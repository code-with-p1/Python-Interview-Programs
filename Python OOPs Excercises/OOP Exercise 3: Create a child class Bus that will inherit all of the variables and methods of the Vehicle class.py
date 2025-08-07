class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

bus = Bus("School Volvo", 180, 12)
print(f"Vehicle Name: {bus.name} Speed: {bus.max_speed} Mileage: {bus.mileage}")