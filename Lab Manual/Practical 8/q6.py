n=int(input("Enter number of elements in list"))
list1=[]
for i in range(n):
    a=int(input("Enter value"))
    list1.append(a)
tuple1=lambda a:(max(a), min(a))
print(tuple1(list1))
