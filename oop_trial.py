class Shapes:
    def __init__(self, name, side, type, size):
        self.name = name
        self.side = side
        self.type = type
        self.size = size

    def area(self):
        print("I am a " + self.name + "\n"
              "I have " + self.side + " sides" "\n"
              "I am a " + self.type + "\n"
              "I am " + self.size + "\n")


obj_shape = Shapes("shape", "4", "polygon", "14cm")
obj_shape.area()


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * self.radius*self.radius
        print(result)


obj_coin = Circle(5)
obj_coin.area()


class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area_triangle = 0.5*(self.base * self.height)
        return area_triangle


obj_pyramid = Triangle(5, 10)
print(obj_pyramid.area())
