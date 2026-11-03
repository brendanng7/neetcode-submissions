class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        while hashset:
            curr = 1
            minNum = maxNum = hashset.pop()
            while (minNum- 1) in hashset or (maxNum + 1) in hashset:
                if (minNum - 1) in hashset:
                    curr += 1
                    hashset.remove(minNum - 1)
                    minNum -= 1
                if (maxNum + 1) in hashset:
                    curr += 1
                    hashset.remove(maxNum + 1)
                    maxNum += 1
            res = max(curr, res)
        
        return res
