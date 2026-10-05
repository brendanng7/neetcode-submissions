class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] is the min number of jumps required to reach there
        # dp[i] = 

        dp = [math.inf] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            maxLength = nums[i]
            for j in range(maxLength + 1):
                if i + j <= len(dp) - 1:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
        print(dp)
        return dp[-1]

            