class Restaurant:
    def __init__(self, name, cuisine_type, num_seats):
        self.name = name
        self.cuisine_type = cuisine_type
        self.num_seats = num_seats
    def get_name(self):
        return self.name
    def get_cuisine_type(self):
        return self.cuisine_type
    def get_num_seats(self):
        return self.num_seats
    def set_name(self, name):
        self.name = name
    def set_cuisine_type(self, cuisine_type):
        self.cuisine_type = cuisine_type
    def set_num_seats(self, num_seats):
        self.num_seats = num_seats
    def print_info(self):
        print("Restaurant Information:")
        print("Name:", self.name)
        print("Cuisine Type:", self.cuisine_type)
        print("Number of Seats:", self.num_seats)
restaurant = Restaurant(name="MacDonalds", cuisine_type="French", num_seats=50)
restaurant.print_info()
