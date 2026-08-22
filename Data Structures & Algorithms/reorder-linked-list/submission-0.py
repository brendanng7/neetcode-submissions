# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # put into a doubly linked list
        # increament l and decrement r pointers until pointing same node
        # O(n)

        arr = deque()
        curr = head
        head = head.next
        while head:
            arr.append(head)
            head = head.next
        
        i = 0
        while arr:
            if i % 2 == 0:
                curr.next = arr.pop()
            else:
                curr.next = arr.popleft()
            curr = curr.next
            i += 1
        curr.next = None
