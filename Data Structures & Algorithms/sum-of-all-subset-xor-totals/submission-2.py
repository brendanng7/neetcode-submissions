class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(currXORSum, idx):
            nonlocal total
            if idx < len(nums):
                backtrack(currXORSum ^ nums[idx], idx + 1)
                backtrack(currXORSum, idx + 1)
            else:
                total += currXORSum
            

        backtrack(0, 0)
        return total

                
        