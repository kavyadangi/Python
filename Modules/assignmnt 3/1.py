from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return pi * self.radius**2
    def calculate_circumference(self):
        return 2 * pi * self.radius
circle = Circle(radius=7)
area = circle.calculate_area()
print("Area:", area)
circumference = circle.calculate_circumference()
print("Circumference:", circumference)
