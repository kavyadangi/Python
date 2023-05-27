class Shape:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.area = None
    def get_info(self):
        return f"Number of Sides: {self.num_sides}, Area: {self.area}"
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(num_sides=3)
        self.base = base
        self.height = height
    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
shape = Shape(num_sides=8)
print(shape.get_info())
triangle = Triangle(base=5, height=10)
print(triangle.get_info())
triangle.calculate_area()
print(triangle.get_info())
