class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use kadane algorithm

        # keep track of currMax, currMin whenever a new element is added

        currMin = currMax = 1
        res = nums[0]
        for num in nums:
            temp = currMax * num
            currMax = max(num, temp, currMin * num)
            currMin = min(num, temp, currMin * num)
            res = max(res, currMax)
        return res

