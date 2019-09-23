class User:

    def __init__(self, name, email): #construct the object of the class
        self.name = name
        self.email = email
        self.type='guest'
        self.password_hash=None

     #  the set password method goes here
    def set_password(self, password):
        self.password_hash=password

    def __repr__(self):
        s="Name: {}, Email: {}, Type: {}, Password {}"
        s= s.format(self.name, self.email, self.type, self.password_hash)
        return s


class Admin(User): # derived class of User
    def __init__(self, name, email):
        super().__init__(name,email) #when you call base class method super()
        self.type='admin'