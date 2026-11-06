class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(it, currSubset, res):

            res.append(currSubset.copy())

            for i in range(it, len(nums)):
                if i > it and nums[i] == nums[i - 1]:
                    continue
                currSubset.append(nums[i])
                backtrack(i+1, currSubset, res)
                currSubset.pop()
            
        backtrack(0, [], res)
        return res