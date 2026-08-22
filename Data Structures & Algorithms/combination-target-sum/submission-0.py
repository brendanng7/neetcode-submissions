class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(it, curr, total):
            if total > target or it >= len(nums):
                return
            elif total == target:
                combinations.append(curr.copy())
            else:
                newCurr = curr.copy()
                newCurr.append(nums[it])
                backtrack(it, newCurr, total + nums[it])
                backtrack(it + 1, curr.copy(), total)
        backtrack(0, [], 0)
        return combinations