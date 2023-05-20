a=int(input("Enter number"))
s=0
def number(a):
    if(a==1):
        print(a)
        return 1
    n=(1+number(a-1))
    print(n)
    return a
number(a)
