names=[]
city=[]
n=int(input("Enter number of record"))
for i in range(0,n,1):
    names.append(input("Enter name of student"))
    city.append(input("Enter city of student"))
dict1=dict(zip(names, city))
for keys, value in dict1.items():
   print(keys)
