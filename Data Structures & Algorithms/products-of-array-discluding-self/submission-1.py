class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [0] * len(nums)
        suffix_arr = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            num = nums[i]
            prefix = prefix * num
            prefix_arr[i] = prefix
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            suffix = suffix * num
            suffix_arr[i] = suffix
    
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_arr[1])
            elif i == len(nums) - 1:
                res.append(prefix_arr[len(nums)-2])
            else:
                res.append(prefix_arr[i-1] * suffix_arr[i+1])

        return res