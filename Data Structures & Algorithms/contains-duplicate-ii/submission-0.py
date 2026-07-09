class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute force solution
        # for each num check if another same num exists then check if it is within k
        # total time is n^2

        # [4,1,2,3,2,1,5] k = 3
        # keep track of l and r
        # use a set to store what numbers are between l and r index
        # initialise l = 0 and r = l + k

        l = 0
        window = set()

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
