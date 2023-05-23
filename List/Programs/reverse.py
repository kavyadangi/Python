#Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
list1=[]
list2=[]
for i in range(0,10,1):
    list1.append(int(input("Enter value")))
for i in range(0,10,1):
    list2.append(list1[9-i])
print(list2)
