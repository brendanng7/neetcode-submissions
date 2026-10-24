import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @functools.cache
        def dfs(i, canRob):
            if i == len(nums):
                return 0
            
            if canRob:
                robbing = dfs(i + 1, not canRob) + nums[i]
                skip = dfs(i + 1, canRob)
                return max(robbing, skip)
            else:
                return dfs(i + 1, not canRob)
        
        return dfs(0, True)
            