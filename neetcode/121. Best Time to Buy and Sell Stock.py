"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


    
Takeaway:

we're main purpose buy low sell high


"""


class Solution:

    # bad try
    def maxProfit_(self, prices: list[int]) -> int:
        min_price: int
        max_price: int

        hash_prices = {}
        for day, price in enumerate(prices):
            hash_prices[price] = day 
        
        min_price = min(hash_prices.items())
        if prices[min_price[1] + 1 :]:
            max_price = max(prices[min_price[1] + 1 :])
            return max_price - min_price[0]
        return 0
    
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l += 1
            r += 1
        
        return max_profit



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([2,4,1]))