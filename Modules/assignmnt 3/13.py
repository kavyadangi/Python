class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def make_sound(self):
        print("Sound!")
    def fetch(self):
        print(f"{self.name}, the {self.breed} dog, is fetching a ball.")
animal = Animal("Cat", "Lion")
animal.make_sound()
dog = Dog("Buddy", "abc", "Labra")
dog.make_sound()
dog.fetch()
