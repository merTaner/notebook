"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, 
she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and 
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109


    
Takeaway:

start value formula : sum of list items // hours


"""
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # we should use l < r  in binary search
        # use math.ceil() because it's necessary for flow numbers
        #
        # [3,6,7,11], h = 8
        #  l          r
        # l, r = 1, max(piles)
        # k size of max(piles)
        # k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        #      l             m                r
        # k = 6, 1h, 2h, 3h, 4h, 5h 
        #        3/6=1 6/6=1 6/7=2 6/11=2 = 6 < h this is true solution
        # but solution would be good more 
        # k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        #      l     m     r
        #
        # continue like this

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11], h=8))
    print(sol.minEatingSpeed([30,11,23,4,20], h=5))
    print(sol.minEatingSpeed([30,11,23,4,20], h=6))