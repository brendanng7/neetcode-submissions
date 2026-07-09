class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        curr = None
        arr = [None] * len(nums)
        for num in nums:
            if curr == None:
                curr = num
                arr[l] = num
                l += 1
            elif curr == num:
                arr[r] = num
                r -= 1
            else:
                curr = num
                arr[l] = num
                l += 1
        print(arr)
        for i in range(len(nums)):
            nums[i] = arr[i]
        return l