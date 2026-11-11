# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l +=1
        print(l)
        cur = ListNode()
        new_h = cur
        cur.next = head
        
        for j in range(l):
            if l-j == n:
                print(j)
                t = cur.next 
                cur.next = cur.next.next
                t.next = None
                break
            cur = cur.next
        return new_h.next


        