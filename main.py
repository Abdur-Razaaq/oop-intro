class Cats:
    def __init__(self, species, name, gender, colour, age):
        self.type = species
        self.name = name
        self.gender = gender
        self.colour = colour
        self.age = age

    def move(self):
        print("I am a: " + self.type + "\n"
              "My name is: " + self.name + "\n"
              "My gender is: " + self.gender + "\n"
              "My colour is: " + self.colour + "\n"
              "My age is: " + self.age + "\n")


objCats = Cats("Lion", "White Lion", "Male", "White", "5-Years-Old")
objCats.name = "Mountain Lion"
objCats.move()


class Lion(Cats):
    pass


class Tiger(Lion):
    pass
