#Question part2: Can we see the different objects respond differently to the
#same method call? if yes/ no explain it in short? and what the usage of this concept?

#Answer: yes because each class has its own method. only attributes were inherited from
#the superclasses

#Defining Superclass
class Animal:
    def __init__(self, name):
        self.name = name

#Defining Child classes
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name) #Inherit/initialize Animal class' attributes
        self.feature = feature

class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name) #Inherit/initialize Animal class' attributes
        self.feature = feature

class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name) #Inherit/initialize Animal class' attributes
        self.feature = feature

class Dog(Mammal):
    def __init__(self, name, feature):
        super().__init__(name, feature) #Inherit/initialize Animal class' attributes

    def walk(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Dog Walk")

class Cat(Mammal):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Inherit/initialize Animal class' attributes

    def walk(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Cat Walk")

class Eagle(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Inherit/initialize Animal class' attributes

    def fly(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Eagle Fly")

class Penguin(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Inherit/initialize Animal class' attributes

    def swim(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Penguin Swim")

class Salmon(Fish):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Inherit/initialize Animal class' attributes

    def swim(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Salmon Swim")

class Shark(Fish):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Inherit/initialize Animal class' attributes

    def swim(self):
        print(f"Name: {self.name}, Feature: {self.feature}, Shark Swim")

if __name__ == "__main__":

    #Define objects for each
    dog = Dog("Dog", "White")
    cat = Cat("Cat", "Black")
    eagle = Eagle("Eagle", "Red")
    penguin = Penguin("Penguin", "Cute")
    salmon = Salmon("Salmon", "Orange")
    shark = Shark("Shark", "Big")

    #Call methods
    dog.walk()
    cat.walk()
    eagle.fly()
    penguin.swim()
    salmon.swim()
    shark.swim()