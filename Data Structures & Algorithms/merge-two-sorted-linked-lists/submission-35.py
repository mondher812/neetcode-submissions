class Solution:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def mergeTwoLists(self, list1, list2):
        h1 = list1
        h2 = list2
       
        head = None
           

        if h1 and h2 and h1.val> h2.val:
            head = h2
            h2 = h2.next
        elif h1 and h2 and h2.val >= h1.val:
            head = h1
            h1 = h1.next
            
          
        if head:
            curr = head

            while h1 and h2:
                if h1.val < h2.val:
                    curr.next = h1
                    h1= h1.next
                    curr = curr.next
                else:
                    curr.next = h2
                    h2= h2.next
                    curr = curr.next
            if h1:
                curr.next = h1
                
            if h2:
                curr.next = h2
        else:
            if h1:
                return h1
            else:
                return h2

        return head




            
