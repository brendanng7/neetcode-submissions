# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr: 
            stack.append(curr)
            curr = curr.next
        
        while n > 0:
            prev = stack.pop()
            n -= 1
        
        if not stack:
            return prev.next
        
        else:
            curr = stack.pop()
            curr.next = curr.next.next
            return head
        