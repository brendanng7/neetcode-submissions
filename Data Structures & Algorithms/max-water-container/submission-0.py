class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            left_h, right_h = heights[l], heights[r]
            max_area = max((r - l) * min(left_h, right_h), max_area)

            if left_h < right_h:
                l += 1
            else:
                r -= 1
        
        return max_area

