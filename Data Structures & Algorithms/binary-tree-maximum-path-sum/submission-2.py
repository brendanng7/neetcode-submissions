# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currMax = -math.inf
        def recurse(root):
            nonlocal currMax
            if not root:
                return -math.inf
            left = recurse(root.left)
            right = recurse(root.right)

            curr = root.val
            total = max(left + curr, curr + right, curr)
            currMax = max(currMax, left, right, total, left + curr + right)
            return total
        
        recurse(root)
        return currMax

        # total = max(left + root + right, left + root, root + right, root)
        # currMax = max(currMax, left, right)