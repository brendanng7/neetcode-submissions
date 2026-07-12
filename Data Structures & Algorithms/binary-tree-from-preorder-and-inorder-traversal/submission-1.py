# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root of the tree is always the preorder 1st
        if not preorder:
            return None
        root = preorder[0]
        inorderIdx = inorder.index(root)

        leftNode = self.buildTree(preorder[1:1+inorderIdx], inorder[:inorderIdx])
        rightNode = self.buildTree(preorder[1+inorderIdx:], inorder[inorderIdx+1:])
        rootNode = TreeNode(val=root, left=leftNode, right=rightNode)
        return rootNode