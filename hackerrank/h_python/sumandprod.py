"""
Sample Input

2 2
1 2
3 4

Sample Output

24

"""

import numpy as np 

matrix_size = list(map(int, input().split()))

arr = np.array([input().split() for _ in range(matrix_size[0])], dtype=int)
print(np.prod(np.sum(arr, axis=0)))

    
