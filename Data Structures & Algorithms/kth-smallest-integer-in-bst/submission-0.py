# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def recurse(root, k):
            nonlocal res
            if not root:
                return 0
            print(root.val, k)
            leftSize = recurse(root.left, k)
            rightSize = recurse(root.right, k - leftSize - 1)
            if leftSize + 1 == k:
                res = root.val
            return leftSize + rightSize + 1
        recurse(root, k)
        return res