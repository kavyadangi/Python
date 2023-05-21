class Student:
    def __init__(a, name, sap_id, marks):
        a.name = name
        a.sap_id = sap_id
        a.marks = marks

    def display(a):
        print("Name: ", a.name)
        print("SAP ID: ", a.sap_id)
        print("Marks (Physics, Chemistry, Mathematics): ", a.marks)
students = []
for i in range(3):
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
