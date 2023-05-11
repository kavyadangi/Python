#WAP to create a function, showemployee, using the following conditions:
#1. Accept employee name and salary an display both.
#2. It the salary is missing in the function call then assign default value 9000 to the salary.
def showemployee(name, salary=9000):
    print("Name :", name)
    print("Salary :", salary)
showemployee("a", 1290)
showemployee("b")
