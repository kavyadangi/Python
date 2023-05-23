#Write a program to find the product of all elements of a list.
list1=[]
prod1=1
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
    prod1*=list1[i]
print(prod1)
