#Initialize and print each element in new line of a list inside list.
list1=[]
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
for i in range(0,n,1):
    print(list1[i])
