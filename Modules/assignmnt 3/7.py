class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_doors(self):
        return self.num_doors
vehicle = Vehicle(make="Tata", model="Tigor", year=2020)
print(vehicle.get_info())
car = Car(make="Honda", model="City V", year=2021, num_doors=4)
print(car.get_info())
print(car.get_doors())
