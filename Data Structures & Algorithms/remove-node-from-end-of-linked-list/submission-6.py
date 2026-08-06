# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = {}
        cur = head
        i = 0
        while cur:
            h[i] = cur
            cur = cur.next
            i+=1
        remove = i-n
        if remove == 0:
            return head.next

       
        tmp = h[remove-1]
        tmp2 = h.get(i-n+1,None)  
        if tmp:
            tmp.next = tmp2
     
        return head

            
        