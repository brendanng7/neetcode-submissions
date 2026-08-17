class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetArr = []

        def backtrack(subsetArr, currSubset, currIndex, allNums):
            if currIndex >= len(allNums):
                subsetArr.append(currSubset)
                return

            noAddSubset = currSubset
            addSubset = currSubset.copy()
            addSubset.append(allNums[currIndex])

            backtrack(subsetArr, noAddSubset, currIndex + 1, allNums)
            backtrack(subsetArr, addSubset, currIndex + 1, allNums)
            
        backtrack(subsetArr, [], 0, nums)
        return subsetArr