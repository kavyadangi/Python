#WAP to create a reccursive function to calculate the sum of numbers from 0 to 10.
def func1(k):
    if(k>0):
        result=k+func1(k-1)
    else:
        result=0
    return result
print(func1(10))
