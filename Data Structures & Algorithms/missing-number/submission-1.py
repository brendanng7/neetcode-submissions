class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumNums = sum(nums)
        sumN = sum(range(n + 1))
        return sumN - sumNums