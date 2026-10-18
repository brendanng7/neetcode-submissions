# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            curr = head = ListNode()
            while list1 or list2:
                if list1 and list2:
                    if list1.val <= list2.val:
                        curr.next = list1
                        list1 = list1.next
                    else:
                        curr.next = list2
                        list2 = list2.next
                elif list1:
                    curr.next = list1
                    list1 = list1.next
                elif list2:
                    curr.next = list2
                    list2 = list2.next
           
                curr = curr.next
            return head.next

        queue = deque(lists)
        while len(queue) > 1:
            list1 = queue.popleft() if queue else None
            list2 = queue.popleft() if queue else None
            newlist = mergeTwoLists(list1, list2)
            queue.append(newlist)
        return queue[0] if lists else None