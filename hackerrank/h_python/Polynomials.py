import numpy as np 

arr = list(map(float, input().split()))
print(np.polyval(arr, int(input())))