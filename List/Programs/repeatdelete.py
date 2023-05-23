#Make a list by taking 10 input from user. Now delete all repeated elements of the list.
#E.g.-
#INPUT : [1,2,3,2,1,3,12,12,32]
#OUTPUT : [1,2,3,12,32]
list1=[]
n=int(input("Enter number of elements in array"))
for i in range(0,n,1):
    list1.append(int(input("Enter value")))
a=list1[0]
for i in range(0,n,1):
    for j in range(0,n,1):
        if(list1[i]==list1[j] and i!=j)
