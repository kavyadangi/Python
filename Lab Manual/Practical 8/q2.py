a=int(input("Enter number"))
def cube(a):
    s=0
    for x in range (a):
        s+=x**3
    return s
print(cube(a))
