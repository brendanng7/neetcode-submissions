# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max diameter is the max of child diameter and sum of its left depth and right depth
        
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0

        leftDepth = 1 + self.dfs(root.left) if root.left else 0
        rightDepth = 1 + self.dfs(root.right)if root.right else 0

        print(root.val, leftDepth, rightDepth)

        self.res = max(leftDepth + rightDepth, self.res)

        return max(leftDepth, rightDepth)