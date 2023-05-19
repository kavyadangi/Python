names=[]
city=[]
n=int(input("Enter number of record"))
for i in range(0,n,1):
    names.append(input("Enter name of student"))
    city.append(input("Enter city of student"))
dict1=dict(zip(names, city))
city_count = {}
for city in dict1.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Number of Students in Each City:")
for city, count in city_count.items():
    print("City: {}, Count: {}".format(city, count))
