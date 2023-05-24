import math
n=float(input("Enter a number"))
if n>=0:
    r=math.sqrt(n)
    print("The square root of", n, "is", r)
else:
    print("Error: Cannot compute square root of a negative number")
