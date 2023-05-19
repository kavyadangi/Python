movies=[] 
n=int(input("enter no of movies")) 
for i in range(0, n, 1): 
    w=input("enter name of the movie:") 
    x=int(input("enter year of  release:")) 
    y=input("enter name of the director:") 
    z=float(input("enter production cost of the movie:")) 
    p=float(input("enter collection made by the movie:")) 
    movie={"name":w,"year":x,"director":y,"production cost":z,"collection":p}
    movies.append(movie)
direcname=input("enter name of director to srch")
print("movies directed by {direcname} are : ")
for movie in movies:
    if movie["director"]==direcname:
        print(movie["name"])
