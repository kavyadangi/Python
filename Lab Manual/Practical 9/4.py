class a:
    def b(z):
        print("A")

class c(a):
    def b(z):
        print("AB")

class d(a):
    def b(z):
        print("ABC")
a = a()
b = c()
c = d()
a.b()
b.b()
c.b()
