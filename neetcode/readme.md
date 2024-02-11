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

- 010.Valid Palindrome
    - greate strings methods : str.isalnum(), filter(), lower() ..
    -
    - new_str[::] == new_str[:: -1] compare to flat and reverse of the list
    -
    - filter(str.isalnum, 'any string')

- 011.Two Sum II - Input Array Is Sorted
    - if you want use two pointer you can use for index :   left, right = 0, len(numbers) - 1
    - 
    - 

- 012.3Sum
    - if you have to chose tree index you should constant one option
    - 
    - and then remaining options bring us to the question of two pointers.
    - 
    - enumerate is very strong method.
    - 
        - l += 1
        - while nums[l] == nums[l - 1] and l < r:
        -   l += 1
    - 
    - If the current number is the same as the previous number, the code moves to the next number.

- 013.Container With Most Water
    - Two pointers keep being the same, define them first and on condition
 increase/ decrease them.
    - 
    - 

- 014.Trapping Rain Water
    - solution of the question was classic two pointer but hard to understand
    - 
    - 

## Stack 

- 015.Valid Parentheses
    - we're using to stack for control to parentesis
    - 
    - if stack is empty we're finished to method

- 016.Min Stack
    - for O(1) time complex, use another stack
    - 
    - beacuse cost of stakcs O(1)

- 017.Evaluate Reverse Polish Notation
    -  think little bit determinant
    - 
    - classic stack methods : pop(), append()

- 018.Generate Parentheses
    - it would be open < n 
    - 
    - would be close < open
    - 
    - it valid if open == close == n