n=int(input("Enter number of entries"))
i=1
list1=[]
while(i<=n):
    list1.append(int(input("please enter a no between 0-3")))
    i=i+1
print(list1)
count0=0
count1=0
count2=0
count3=0
for i in range(0,n,1):
    if(list1[i]==0):
        count0+=1
    elif(list1[i]==1):
        count1+=1
    elif(list1[i]==2):
        count2+=1
    elif(list1[i]==3):
        count3+=1
print("Number of 0's occured are :", count0)
print("Number of 1's occured are :", count1)
print("Number of 2's occured are :", count2)
print("Number of 3's occured are :", count3)
