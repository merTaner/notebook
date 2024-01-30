## Arrays & Hashing


- 001.Contains Duplicate
    - used Counter() method
    -
    -

- 002.Valid Anagram
    - if you work with dictionary you should know get() item method. 
    -
    -

- 003.Two Sum
    - enumerate is powerfull.
    - 
    - I used fewer variables thanks to enumerate

- 004.Group Anagrams
    - don't forget to while work with dictionary you use sub-list for each item. 
    -
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

- 009.Encode and Decode Strings
    - use only one charter for sperate strings. This time we have a problem.
    -
    - example -> ['mert', 'mert:;taner'] if we have like this list we during encode and decode
    -
    - decode is never assing to original list. encode = 'mert:;mert:;taner;;' okay but decoder = ['mert', 'mert', 'taner']
    -
    - res += str(len(s)) + '#' + s -> perfect way for sign