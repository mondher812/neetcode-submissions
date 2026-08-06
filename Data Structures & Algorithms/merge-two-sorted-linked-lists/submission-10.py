# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        
        # handle empty input cases
        if not h1:
            return h2
        if not h2:
            return h1
        
        # initialize new and head
        if h1.val > h2.val:
            new = h2
            h2 = h2.next
        else:
            new = h1
            h1 = h1.next
        
        head = new
        
        # merge loop
        while h1 and h2:
            if h1.val > h2.val:
                new.next = h2
                new = new.next
                h2 = h2.next
            else:
                new.next = h1
                new = new.next
                h1 = h1.next
        
        if h1:
            new.next = h1
        if h2:
            new.next = h2
        
        return head

               