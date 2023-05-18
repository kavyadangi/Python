import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.sum(arr, axis=1)
col = np.sum(arr, axis=0)
max2 = np.sort(np.unique(arr))[-2]
print("Array:\n", arr)
print("Row sum:", row)
print("Column sum:", col)
print("Second maximum element:", max2)
