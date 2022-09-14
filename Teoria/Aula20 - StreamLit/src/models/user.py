class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f'User(Name:{self.name}, Email:{self.email}, Password:{self.password})'