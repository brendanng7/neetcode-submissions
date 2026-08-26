class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIndex = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= currIndex:
                currIndex = i
        
        return nums[0] >= currIndex