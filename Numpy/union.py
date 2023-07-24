import numpy as np
n=np.array([10,20,30,40,50])
n1=np.array([20,40,60,80,100])
n2=np.union1d(n,n1)
print(n2)
