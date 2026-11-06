class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def backtrack(it, currCombination, res, currSum):
            if currSum > target:
                return

            if currSum == target:
                res.append(currCombination.copy())
            
            for i in range(it, len(candidates)):
                if i > it and candidates[i] == candidates[i - 1]:
                    continue
                currCombination.append(candidates[i])
                backtrack(i+1, currCombination, res, currSum + candidates[i])
                currCombination.pop()
        
        backtrack(0, [], res, 0)
        return res