# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        total_n= 0
        c = head
        while c:
            total_n+=1
            c =c.next
        i = 0
        to_reat = ListNode()
        c = head
        to_reat.next = head
        c =head
        prev = to_reat
        while i <total_n and c is not None:
            if i == total_n - n:
                prev.next = c.next
                c.next = None

            else:
                prev = c
                c = c.next
            i+=1
        return to_reat.next
