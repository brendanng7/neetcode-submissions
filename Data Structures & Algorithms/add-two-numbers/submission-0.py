# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ten = 0
        curr = res = ListNode()
        while l1 or l2 or ten:
            if l1:
                curr.val = curr.val + l1.val
                l1 = l1.next
            if l2:
                curr.val = curr.val + l2.val
                l2 = l2.next
            curr.val = curr.val + ten
            remainder = curr.val % 10
            if curr.val - remainder > 0:
                ten = int((curr.val - remainder) / 10)
            else:
                ten = 0
            curr.val = remainder
            if l1 or l2 or ten:
                nextnode = ListNode()
                curr.next = nextnode
                curr = curr.next
        return res

        