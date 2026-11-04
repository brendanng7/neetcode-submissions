import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @functools.cache
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            minCoins = math.inf
            for coin in coins:
                res = dfs(amount - coin)
                minCoins = min(res + 1, minCoins)
            
            return minCoins
        
        res = dfs(amount)
        if res == math.inf:
            return -1
        else:
            return res
            