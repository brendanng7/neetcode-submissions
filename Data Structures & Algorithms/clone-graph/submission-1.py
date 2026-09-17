"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        root = Node(node.val, [])
        old_to_new[node] = root
        queue = deque()
        queue.append(node)

        while queue:
            old = queue.popleft()
            for n in old.neighbors:
                if n not in old_to_new:
                    new_n = Node(n.val, [])
                    old_to_new[n] = new_n
                    queue.append(n)
                old_to_new[old].neighbors.append(old_to_new[n])
        
        return root
            

            
        