lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
x=lst[0]
for a in lst:
    if(x<a and a!=max(lst)):
        x=a
print(x)
