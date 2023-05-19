n = int(input("Enter the number of values: "))
list1 = []
for i in range(n):
    value = float(input("Enter value"))
    list1.append(value)
tuple1=tuple(list1)
sum = 0
for value in tuple1:
    sum += value
print(sum / len(tuple1))
