class Cat:
    def __inner__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color} {self.age}'

    def fun(self):
        print("Soy un gato de color", self.color, "y hago miu")



