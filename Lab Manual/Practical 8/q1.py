n=int(input("Enter number of elements"))
list1=[]
for i in range(n):
    a=int(input("Enter value"))
    list1.append(a)
def max(a):
    b=a[0]
    for i in range(len(a)):
        if(b<a[i]):
           b=a[i]
    return b
def min(a):
    b=a[0]
    for i in range(len(a)):
        if(b>a[i]):
           b=a[i]
    return b
print("Max =", max(list1))
print("Min =", min(list1))
