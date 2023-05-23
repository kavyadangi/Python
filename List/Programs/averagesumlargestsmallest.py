#Write a program to print sum, average of all numbers, smallest and largest element of a list.
#Find largest and smallest elements of a list.
list1=[]
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
smallest=list1[0]
largest=list1[0]
for i in range(0,n,1):
    if(smallest>list1[i]):
        smallest=list1[i]
    if(largest<list1[i]):
        largest=list1[i]
print("Largest element in list =", largest)
print("Smallest element in list =", smallest)
