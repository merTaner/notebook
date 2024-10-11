class Solution:
    def longestCommonPrefix_(self, strs: list[str]) -> str:
        # we can use zip too!
        # this might be the fastest
        res = ""
        for a in zip(*strs):
            # this zips all input in a single indexed element
            # zip([hello, dog, cat]) -> [(h, d, c), (e, o ,g) ...]
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res

    def longestCommonPrefix__(self, strs: list[str]) -> str:
        # another approach
        res = ""

        # this could be not the shortest
        # but we will deal with it later
        for i in range(len(strs[0])):
            for s in strs:
                # index is out of bounds
                # or
                # character not matching
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

sol = Solution()
print(sol.longestCommonPrefix_(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix_(strs = ["dog","racecar","car"]))
print(sol.longestCommonPrefix_(strs = ["plow", "flower", "flight"]))
print(sol.longestCommonPrefix_(strs = ["grow", "grown", "growth"]))

print()

print(sol.longestCommonPrefix__(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix__(strs = ["dog","racecar","car"]))
print(sol.longestCommonPrefix__(strs = ["plow", "flower", "flight"]))
print(sol.longestCommonPrefix__(strs = ["grow", "grown", "growth"]))