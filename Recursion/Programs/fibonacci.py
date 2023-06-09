#Use recursion to print fibonacci series
a=int(input("Enter number"))
def fibonacci(a):
    if(a==1):
        return 0
    elif(a==2):
        return 1
    return(fibonacci(a-1)+fibonacci(a-2))
print(fibonacci(a))
