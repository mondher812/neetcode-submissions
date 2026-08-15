# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = {}
        n = 0
        cur = head

        while cur:
            h[n] = cur
            cur = cur.next
            n+=1
        out_h = head
        print(n)
        l = 1
        r = n -1
        for i in range(n-1):
            if i % 2 == 0:
                out_h.next = h[r]
                r-=1
            else:
                out_h.next = h[l]
                l+=1
               
            out_h = out_h.next
        out_h.next = None
            



        