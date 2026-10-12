class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        secondslow = 0
        while slow != secondslow:
            slow = nums[slow]
            secondslow = nums[secondslow]
        
        return slow