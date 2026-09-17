class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftmax, rightmax = height[l], height[r]
        total = 0

        while l < r:
            if leftmax < rightmax:
                l += 1
                total += max(leftmax-height[l], 0)
                leftmax = max(leftmax, height[l])
            else:
                r -= 1
                total += max(rightmax-height[r], 0)
                rightmax = max(rightmax, height[r])
        
        return total
