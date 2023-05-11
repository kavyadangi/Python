#WAP to create function, function1, to accept a variable length of arguments and print their value.
def function1(*length):
    for i in range(0, len(length), 1):
        print(length[i])
function1("a", "b", "c")
