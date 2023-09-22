x="awesome"                              #global variable
def myfunc():
    x="fantastic"                        #local variable
    print("Python is "+x)
myfunc()                                 #print with local variable
print("Python is "+x)                    #print with global variable
    
