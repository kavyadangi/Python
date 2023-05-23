#Write a program to check if elements of a list are same or not it read from front or back. E.g.-
#2	3	15	15	3	2
list1=[]
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
a=list1[0]
for i in range(0,n,1):
    for j in range(0,n,1):
        if(list1[i]==list1[j] and i!=j):
            del list1[j]
            n=n-1
            print("A")
            continue
        if(a>list1[i]):
            t=a
            a=list1[i]
            list1[i]=t
print(list1)
