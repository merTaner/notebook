"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictionary = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            # it have in dict ?
            if sorted_string not in dictionary:
                # because we solution is have intertwined lists. 
                dictionary[sorted_string] = []

            dictionary[sorted_string].append(string)   

        return list(dictionary.values())    

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams(strs=[""]))
    print(sol.groupAnagrams(strs=["a"]))
    print(sol.another_group_anagrams(strs=["eat","tea","tan","ate","nat","bat"]))