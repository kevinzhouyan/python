class Animal():
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("My name is " + self.name)

class Cat(Animal):
    def __init__(self, name, color, size):
        super().__init__(name)
        self.color = color
        self.size = size
        self.type = "cat"

    def bark(self):
        super().bark()
        print("I'm a " + self.size + " " + self.color + " " + self.type)

class BettaFish(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.type = "betta fish"

    def bark(self):
        super().bark()
        print("I'm a " + self.color + " " +  self.type)

MyBetta = BettaFish("welpy", "blue")
MyBetta.bark()

MyCat = Cat("anna", "yellow", "small")
MyCat.bark()