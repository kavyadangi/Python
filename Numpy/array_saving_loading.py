import numpy as np
n=np.array([10,20,40,50,60,8,58])
a=np.save('array_with_zeroes',n)
b=np.load('array_with_zeroes',n)
print(b)
