
from dataclasses import dataclass

@dataclass
class User:
    Email:str
    Name:str 

@dataclass
class UserRegistrationService:
    Users = []

    def Find(self, email):
        for user in self.Users:
            if user.Email == email:
                return user
        return None

    def Register(self, email, name):
        user = self.Find(email)
        print(user)
        if user == None:
            self.Users.append(User(email,name))
            return True
        return False        

    