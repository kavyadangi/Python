class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
    def print_grade_summary(self):
        print("Grades for", self.name)
        if len(self.grades) == 0:
            print("No grades available.")
        else:
            print("Number of grades:", len(self.grades))
            print("Grades:", ", ".join(map(str, self.grades)))
            print("Average grade:", self.calculate_average_grade())
student = Student(name="Kavya", id_number="500108583")
student.add_grade(90)
student.add_grade(92)
student.add_grade(78)
student.add_grade(85)
student.print_grade_summary()
