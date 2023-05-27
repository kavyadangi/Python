class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("The animal makes a sound")
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def fetch(self):
        print("The dog fetches a ball")
animal = Animal(name="Cat", species="Tiger")
print(animal.name)
print(animal.species)
animal.make_sound()
dog = Dog(name="Buddy", species="abc", breed="Labra")
print(dog.name)
print(dog.species)
print(dog.breed)
dog.make_sound()
dog.fetch()
