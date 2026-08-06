# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        new_h = ListNode(-1,None)
        h = {}
        i = 0
        for listhead in lists:
            h[i] = listhead
            i+=1
        next_min = float('inf')
        to_change = 0
        real_h = ListNode(0,None)
        new_h.next = real_h
        k = 0
        
        while to_change < i:
            for j in range(len(h)):
                if  h[j] and h[j].val <= next_min:
                    next_min = h[j].val
                    k = j
            if h[k]:
                real_h.next = h[k]
                if h[k].next == None:
                    to_change +=1
                h[k] = h[k].next
                real_h = real_h.next
            next_min = float('inf')

        return new_h.next.next
        
        
        