import numpy as np 

n, *args = input().split()
arr = [np.array(input().split(), dtype=int) for _ in range(int(n))]

print(np.max(np.min(arr, axis=1)))
    


