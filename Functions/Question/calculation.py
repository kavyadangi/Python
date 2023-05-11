#WAP to create a function, calculation, such that it can accept two variables and calcuate addition and subtraction. Also it must return both addition and subtraction in a single return call.
def calculation(a, b):
    return a+b, a-b
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(calculation(a,b))
