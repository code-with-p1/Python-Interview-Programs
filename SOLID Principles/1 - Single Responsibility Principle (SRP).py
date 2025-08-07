'''

Single Responsibility Principle (SRP): 

A class should have only one reason to change, meaning it should have only one responsibility or job. 
This principle promotes modularization and separation of concerns, making classes easier to understand and maintain.

'''

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)
    
    def get_user_by_email(self, email):
        for user in self.users:
            if user.get_email() == email:
                return user
        return None
