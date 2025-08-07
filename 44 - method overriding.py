class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call the make_sound method
animal.make_sound()  # Output: Generic animal sound
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
