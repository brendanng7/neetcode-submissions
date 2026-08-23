class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(it, curr, total):
            if total == target:
                combinations.append(curr.copy())
            elif total > target or it >= len(candidates):
                return
            else:
                newCurr = curr.copy()
                newCurr.append(candidates[it])
                backtrack(it + 1, newCurr, total + candidates[it]) 
                j = it
                while j < len(candidates) and candidates[j] == candidates[it]:
                    j += 1
                backtrack(j, curr.copy(), total)
        backtrack(0, [], 0)
        return combinations