class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # lccatp
        # catncafcajt

        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i, letter1 in enumerate(text1):
            for j, letter2 in enumerate(text2):
                if letter1 == letter2:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        
        
        return dp[len(text1)-1][len(text2)-1]
