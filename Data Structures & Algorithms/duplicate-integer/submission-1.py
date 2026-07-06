class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if (hash.get(num)):
                return True
            else:
                hash[num] = True
        return False