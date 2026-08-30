class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def backtrack(it, curr, res):
            if it == len(nums):
                res.add(tuple(curr))
            else:
                backtrack(it + 1, curr.copy(), res)
                newCurr = curr.copy()
                newCurr.append(nums[it])
                backtrack(it + 1, newCurr, res)
        
        backtrack(0, [], res)
        res = [list(x) for x in list(res)]
        return res