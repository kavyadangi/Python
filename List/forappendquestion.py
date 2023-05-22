#Based on a list of items you want to create a new list containing only those items with letter a in the name
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
