import math
n=int(input("Enter a positive integer"))
if n>=0:
    a=math.factorial(n)
    print("The factorial of", n, "is", a)
else:
    print("Error: Cannot compute factorial of a negative number")
