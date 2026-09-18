class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[low] < nums[mid] and nums[mid] < nums[high]:
                return nums[low]
            else:
                if nums[mid] < nums[high]:
                    high = mid
                else:
                    low = mid + 1
        
        return nums[low]