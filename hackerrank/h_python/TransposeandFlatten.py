"""
Transpose

We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.

import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]
Flatten

The tool flatten creates a copy of the input array flattened to one dimension.

import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]
Task

You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
"""

import numpy as np 

N,M = input().split()

arr = np.array([input().split() for _ in range(int(N))], dtype=int)

print(np.transpose(arr), arr.flatten(), sep='\n')