# Public: Variables or methods without any leading underscores.
# Protected: Variables or methods with a single leading underscore.
# Private: Variables or methods with double leading underscores.

class MyClass:
    def __init__(self, public_var, _protected_var, __private_var):
        self.public_var = public_var            # public variable
        self._protected_var = _protected_var    # protected variable
        self.__private_var = __private_var      # private variable

    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

# Creating an instance of MyClass
obj = MyClass("public", "protected", "private")

# Accessing public variables and methods
print("Public variable:", obj.public_var)
obj.public_method()

# Accessing protected variables and methods (though discouraged)
print("Protected variable:", obj._protected_var)
obj._protected_method()

# Accessing private variables and methods (will throw an error)
# print("Private variable:", obj.__private_var)  # This will give an AttributeError
# obj.__private_method()  # This will give an AttributeError

# Accessing private variables and methods using name mangling
print("Private variable using name mangling:", obj._MyClass__private_var)
obj._MyClass__private_method()
