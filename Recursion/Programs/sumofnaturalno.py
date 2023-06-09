#Use recursion to print sum on n natural numbers
a=int(input("Enter number"))
s=0
def sum1(a):
    if(a==1):
        return 1
    return(a+sum1(a-1))
print(sum1(a))
