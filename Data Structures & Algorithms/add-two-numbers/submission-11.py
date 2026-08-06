# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        head = ListNode(0,None)
        preval = 0
        new = head
        while cur1 and cur2:
            to_a = cur1.val + cur2.val + preval
            tval = cur1.val + cur2.val + preval
            if to_a >9:
                to_a = to_a%10
                preval = 1
            else:
                preval = 0

            tmp = ListNode(to_a,None)
            new.next = tmp
            new = new.next
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            if cur1.val + preval > 9:
                new.next = ListNode(0,None)
            else:
                new.next = ListNode(cur1.val+preval,None)
                preval = 0

            new = new.next
            cur1 = cur1.next
        while cur2:
            if cur2.val + preval > 9:
                new.next = ListNode(0,None)
            else:
                new.next = ListNode(cur2.val+preval,None)
                preval = 0
            new = new.next
            cur2 = cur2.next
        if preval >0:
            new.next = ListNode(1,None)
        return head.next
        