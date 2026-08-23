class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if len(dp) > coin:
                dp[coin] = 1
        
        for i in range(amount + 1):
            if dp[i] != -1:
                continue
            else:
                minCoin = math.inf
                for coin in coins:
                    if i - coin <= 0:
                        continue
                    else:
                        minCoin = min(minCoin, 1 + dp[i - coin])
                dp[i] = minCoin
        print(dp)
        return dp[amount] if dp[amount] != math.inf else -1