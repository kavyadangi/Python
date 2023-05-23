#Write a program to find the sum of all elements of a list.
list1=[]
sum1=0
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
    sum1+=list1[i]
print(sum1)
