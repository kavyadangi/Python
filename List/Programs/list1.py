#Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s
list1=[]
for i in range(0,20,1):
    list1.append(int(input("Enter value")))
positive=0
negative=0
odd=0
even=0
number0=0
for i in range(0,20,1):
    if(list1[i]>0):
        positive+=1
    elif(list1[i]<0):
        negative+=1
    elif(list1[i]==0):
        number0+=1
    if(list1[i]%2==0):
        even+=1
    elif(list1[i]%2!=0):
        odd+=1
print("Number of positive numbers", positive)
print("Number of negative numbers", negative)
print("Number of odd numbers", odd)
print("Number of even numbers", even)
print("Number of 0s", number0)
