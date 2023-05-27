class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major
    def get_major(self):
        return self.major
person = Person(name="Kavya", age=19, gender="Female")
print(person.get_info())
student = Student(name="Sam", age=19, gender="Male", major="Computer Science")
print(student.get_info())
print(student.get_major())
