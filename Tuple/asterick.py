#the number of variables must match the number of values in the tuple, if not,
#you must use an asterisk to collect the remaining values as a list
fruits=("apple","banana","cherry","strawberry","melon")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
