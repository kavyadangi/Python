#the expression in comprehension syntax can also contain conditions not like the filter but as a way to manipulate the outcome. For eg, return orange instead of banana
fruits=["apple", "cherry", "kiwi", "mango"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)                                  #list comprehension
