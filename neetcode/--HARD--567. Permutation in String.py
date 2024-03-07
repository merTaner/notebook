"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.



Takeaway:

we need number of each charter for per string
and then we compare that results.

comparing a sliding window for the target string can be an approach

"""


class Solution:
    # it's not working I want just try
    def checkInclusion_(self, s1: str, s2: str) -> bool:
            frequencies = {}

            for k, v in enumerate(s2):
                frequencies[v] = frequencies.get(v, 0) + 1

            frequencies2 = {}
            for k, v in enumerate(s1):
                frequencies2[v] = frequencies2.get(v, 0) + 1


            counter: int = 0
            for char, freq in frequencies2.items():
                if char in frequencies.keys():
                    if freq >= frequencies.get(char, 0):
                        counter += 1

                        if counter == len(s1):
                            return True
                
            return False
            
    def checkInclusion(self, s1: str, s2: str) -> bool:  
        
        # O(26.n) because we use just a-z english letters.
        # check if the length of s1 is greater than the length of s2. If it is, 
        # then you can immediately return False because s2 
        # cannot contain a permutation of s1.
        if len(s1) > len(s2) : return False
        
        # character counts for s1 and s2
        s1_count, s2_count = [0] * 26 , [0] * 26

        # iterate over s1
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # calculate the number of matches between s1_count and s2_count
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            # if matches is 26, there is a permutation
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")

            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1
        
        return matches == 26

        

        












if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))




