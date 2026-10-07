import functools
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def backtrack(it, totalsum, num):
            if it == len(nums):
                if totalsum == target:
                    return num + 1
                return 0
            else:
                a = backtrack(it + 1, totalsum + nums[it], num)
                b = backtrack(it + 1, totalsum - nums[it], num)
                return a + b

        return backtrack(0, 0, 0)
        