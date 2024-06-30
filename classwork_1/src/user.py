class User:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 2

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 0
        return self.age