#Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
#( Iterate over list using while loop )
list1=[]
flag=0
for i in range(0,10,1):
    list1.append(int(input("Enter value")))
a=int(input("Enter element to be searched"))
for i in range(0,10,1):
    if(list1[i]==a):
        flag=1
        break
if(flag==1):
    print("Integer found")
elif(flag==0):
    print("Integer not found")
