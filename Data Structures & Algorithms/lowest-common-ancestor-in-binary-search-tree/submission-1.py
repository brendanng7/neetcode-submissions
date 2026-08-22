# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        phat = root
        qhat = root
        
        while phat == qhat:
      
            anc = phat
            if p.val < phat.val:
                phat = phat.left
            elif p.val > phat.val:
                phat = phat.right
            
            if q.val < qhat.val:
                qhat = qhat.left
            elif q.val > qhat.val:
                qhat = qhat.right

            if phat != qhat:
                return anc
                
            
            
           

        

