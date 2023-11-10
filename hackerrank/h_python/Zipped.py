"""
This function returns a list of tuples. The i'th tuple contains the

i'th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is 
truncated to the length of the shortest argument sequence. 

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
"""

number_of_marks, range_of_student = map(int, input().split())

marks = [list(map(float, input().split())) for _ in range(range_of_student)]
    
# marks = [[89 90 78 93 80], [90 91 85 88 86], [91 92 83 89 90.5]]
# student1 = (89, 90, 91)
for student_marks in zip(*marks):
    print(sum(student_marks) / range_of_student)