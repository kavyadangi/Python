movies=[]
a=int(input("enter no of movies"))
for i in range(a):
    w=input("enter name of the movie:")
    x=input("enter year of  release:")
    y=input("enter name of the director:")
    z=float(input("enter production cost of the movie:"))
    p=float(input("enter collection made by the movie:"))
    movie={"name":w,"year":x,"director":y,"production cost":z,"collection":p}
    movies.append(movie)
print("all details of movie:")
for movie in movies:
    print(movie)
