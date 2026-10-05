# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            currNode, level = queue.popleft()
            if level == len(result):
                result.append(currNode.val)
            else:
                result[level] = currNode.val
            if currNode.left:
                queue.append((currNode.left, level + 1))
            if currNode.right:
                queue.append((currNode.right, level + 1))
        
        return result