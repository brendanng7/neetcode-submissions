class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resultSet = []
        
        for i, num in enumerate(nums[:-2]):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                currTrip = [nums[i], nums[l], nums[r]]
                currSum = sum(currTrip)
                if currSum == 0:
                    if currTrip not in resultSet:
                        resultSet.append(currTrip)
                    l += 1
                elif currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
        
        return list(resultSet)