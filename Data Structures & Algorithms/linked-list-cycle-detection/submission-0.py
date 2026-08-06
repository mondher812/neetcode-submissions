# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        to_check = set()
        cur = head
        while cur:
            if cur in to_check:
                return True
            else:
                to_check.add(cur)
            cur = cur.next
        return False