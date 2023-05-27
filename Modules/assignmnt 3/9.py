class Shape:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.area = 0
    def get_info(self):
        return f"This shape has {self.num_sides} sides and an area of {self.area} units."
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(num_sides=3)
        self.base = base
        self.height = height
    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
triangle = Triangle(base=10, height=5)
print(triangle.num_sides)
print(triangle.base)
print(triangle.height)
print(triangle.area)
triangle.calculate_area()
print(triangle.area)
print(triangle.get_info())
