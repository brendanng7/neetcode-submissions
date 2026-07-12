class Solution:
    total = 0
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(currXORSum, idx):
            if idx < len(nums):
                backtrack(currXORSum ^ nums[idx], idx + 1)
                backtrack(currXORSum, idx + 1)
            else:
                self.total += currXORSum
            

        backtrack(0, 0)
        return self.total

                
        