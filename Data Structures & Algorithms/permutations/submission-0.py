class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        # [1, 2, 3, 4, 5]
        def backtrack(curr, remaining):
            if len(curr) == len(nums):
                permutations.append(curr)
            else:
                for i in range(len(remaining)):
                    num = remaining[i]
                    newCurr = curr.copy()
                    newCurr.append(num)
                    newRemaining = remaining.copy()
                    newRemaining.pop(i)
                    backtrack(newCurr, newRemaining)
        backtrack([], nums)
        return permutations