# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        t = None
        second = slow.next
        slow.next = None
        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t 
        first = head
        second = prev
        while second:
            t1 = second.next
            t2 = first.next
            first.next = second
            second.next =t2
            second  = t1
            first = t2

