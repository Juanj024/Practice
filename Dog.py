
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def fun(self):
        print(self.name,"Ese es mi nombre chavalines")
