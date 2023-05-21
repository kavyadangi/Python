class Student:
    def __init__(a, name, sap_id, marks):
        a.name = name
        a.sap_id = sap_id
        a.marks = marks

    def display(a):
        print("Name: ", a.name)
        print("SAP ID: ", a.sap_id)
        print("Marks (Physics, Chemistry, Mathematics): ", a.marks)

    def percent(a):
        total = sum(a.marks)
        percentage = total / len(a.marks)
        return percentage

    def display(a):
        percentage = a.percent()
        result = "Pass" if percentage > 40 else "Fail"
        print("Result: ", result)

   
    def average(students):
        total = 0
        num = len(students)
        for student in students:
            total += sum(student.marks)
        average = total / (num * len(student.marks))
        return average
students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    print("Enter details for Student", {i+1})
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    marks = []
    for subject in ["Physics", "Chemistry", "Mathematics"]:
        marks.append(int(input(f"Enter marks for {subject}: ")))
    student = Student(name, sap_id, marks)
    students.append(student)
print("Details of all students:")
for i, student in enumerate(students):
    student.display()
    percentage = student.percent()
    print("Marks Percentage: ",percentage)
    student.display()
avg = Student.average(students)
print("Average marks of the class: ", avg)
