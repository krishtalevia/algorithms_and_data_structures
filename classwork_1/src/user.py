class User:
    count = 0

    def __init__(self, name, age):
        self.is_data_valid(name, age)

        self.name = name
        self.age = age
        User.count += 1

    def is_data_valid(self, name, age):
        if not isinstance(age, int):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()

        if age < 0 or age > 150:
            raise ValueError()

        if not name or not age:
            raise ValueError()

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 1
        return self.age