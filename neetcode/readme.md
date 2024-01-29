## Arrays & Hashing


- 001.Contains Duplicate
    - 

- 002.Valid Anagram
    - 

- 003.Two Sum
    - enumerate is powerfull.
    - 
    - I used fewer variables thanks to enumerate

- 004.Group Anagrams
    -

- 005.Top K Frequent Elements
    - Never forget power of dictionary!
    -
    - Slice is very important
    -
    - Nested lists can be used to for items indexing 

- 006.Product of Array Except Self
    - If you multiply every element to the left and to the right, you will get the product of all elements.
    - 
    - res = [1] * len(nums) : somecases this method can be faster than empty list.
    -
    - 

- 007.Valid Sudoku
    - collections.defualt() : Return a new dictionary-like object. defaultdict is a subclass of the built-in dict class.
    - 
    - 

- 008.Longest Consecutive Sequence
    - use set() beacuse don't need to repeat numbers
    - 
    - current = max(current, number)