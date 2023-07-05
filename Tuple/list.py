#updating a tuple: first tuple is supposed to be converted in the list
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)
print(type(x))
