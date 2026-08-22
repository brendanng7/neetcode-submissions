# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow
        tmp = None
        while second:
            nextNode = second.next
            second.next = tmp
            tmp = second
            second = nextNode
        
        start = ListNode(-1)
        curr = start
        list1 = head
        list2 = tmp
        while list1 and list2:
            curr.next = list1
            list1 = list1.next
            curr.next.next = list2
            list2 = list2.next
            curr = curr.next.next
        curr.next = None
        
