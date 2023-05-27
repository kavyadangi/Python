class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_width(self):
        return self.width
    def set_width(self, width):
        self.width = width
rectangle = Rectangle(length=6, width=4)
print("Length:", rectangle.get_length())
rectangle.set_length(10)
print("Length:", rectangle.get_length())
print("Width:", rectangle.get_width())
rectangle.set_width(8)
print("Width:", rectangle.get_width())
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
