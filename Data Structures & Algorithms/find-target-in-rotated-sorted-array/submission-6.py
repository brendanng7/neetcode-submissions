import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid 
        
        left = bisect.bisect_left(nums, target, lo=0, hi=l)
        right = bisect.bisect_left(nums, target, lo=l, hi=len(nums))
        print(left, right)
        if nums[left] == target:
            return left
        if right < len(nums) and nums[right] == target:
            return right
        else:
            return -1
        