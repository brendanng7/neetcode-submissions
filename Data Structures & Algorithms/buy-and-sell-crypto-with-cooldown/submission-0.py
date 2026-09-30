import functools

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @functools.cache
        def dfs(i, hasCoin):
            if i >= len(prices):
                return 0
            hold = dfs(i + 1, hasCoin)
            if hasCoin:
                sell = dfs(i + 2, not hasCoin) + prices[i]
                return max(sell, hold)
            else:
                buy = dfs(i + 1, not hasCoin) - prices[i]
                return max(buy, hold)
        return dfs(0, False)            

