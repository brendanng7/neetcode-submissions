# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, currmax):
            isGoodNode = 1 if curr.val >= currmax else 0

            newmax = max(curr.val, currmax)
            if curr.left and curr.right:
                return dfs(curr.left, newmax) + dfs(curr.right, newmax) + isGoodNode
            elif curr.left:
                return dfs(curr.left, newmax) + isGoodNode
            elif curr.right:
                return dfs(curr.right, newmax) + isGoodNode
            else:
                return isGoodNode
            
        return dfs(root, -101)
        # use dfs, tracking the max in the stack