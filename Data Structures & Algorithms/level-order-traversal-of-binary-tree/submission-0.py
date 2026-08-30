# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        queue = deque()
        queue.append((root, 0))
        
        while queue:
            currNode, level = queue.popleft()

            if len(res) - 1 < level:
                res.append([])
            
            res[level].append(currNode.val)

            if currNode.left:
                queue.append((currNode.left, level + 1))
            
            if currNode.right:
                queue.append((currNode.right, level + 1))
        
        return res