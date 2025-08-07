class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year  # Private attribute

    # Getter Methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
    
    def get_car_info(self):
        return f" Make ({self.__make}), Model({self.__model}) & Year ({self.__year})"

    # Setter Methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

# Usage
print("-"*100)
car = Car("Toyota", "Camry", 2022)
print("Car Make:", car.get_make())
print("Car Model:", car.get_model())
print("Car Year:", car.get_year())
print("Car Info:", car.get_car_info())
print("-"*100)

car.set_year(2023)
print("Updated Car Year:", car.get_year())
print("-"*100)
