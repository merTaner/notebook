"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


    
Takeaway:


"""

class Solution:
    # not bad solution but it's work same test cases
    def lengthOfLongestSubstring_(self, s: str) -> int:
        
        memorize_stack = [] 
        max_lenght = 0
        for c in s:

            if c in memorize_stack: 
                max_lenght = max(max_lenght, len(memorize_stack))
                memorize_stack.clear()
                memorize_stack.append(c)

            if memorize_stack:

                if c not in memorize_stack:
                    memorize_stack.append(c)  

            else:
                memorize_stack.append(c)
                

        return max_lenght

    # neet solution
    def lengthOfLongestSubstring(self, s: str) -> int:       
        # use set for uniq value
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res

    # basic solution
    def lengthOfLongestSubstring__(self, s: str) -> int:
        return len(set(s))



if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "abcabcbb"))
    print(sol.lengthOfLongestSubstring(s = "bbbbb"))
    print(sol.lengthOfLongestSubstring(s = "pwwkew"))
    print(sol.lengthOfLongestSubstring(s = " "))
    print(sol.lengthOfLongestSubstring(s = ""))
