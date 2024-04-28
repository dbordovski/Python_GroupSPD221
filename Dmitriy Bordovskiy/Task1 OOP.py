class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            if int(value) == value:
                self.__age = value
            else:
                print("age is not correct")
        else:
            print("age is not correct")


user = User('Ivan', 40)
print(user.name, user.age)
user.age = 45
print(user.name, user.age)