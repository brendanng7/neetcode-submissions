"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        root = Node(head.val)
        old_to_new[head] = root
        queue = deque()
        queue.append(head)
        while queue:
            old = queue.popleft()
            next_old = old.next
            random_old = old.random
            if next_old not in old_to_new:
                next_new = Node(next_old.val) if next_old else None
                old_to_new[next_old] = next_new
            if next_old:
                queue.append(next_old)
            
            if random_old not in old_to_new:
                random_new = Node(random_old.val) if random_old else None
                old_to_new[random_old] = random_new

            old_to_new[old].next = old_to_new[next_old]
            old_to_new[old].random = old_to_new[random_old]
        
        return root

