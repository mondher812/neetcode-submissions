class Solution:
    def mergeTwoLists(self, list1, list2):
        h1 = list1
        h2 = list2
        real_h = ListNode(-1,None)
        if h1 and h2:
            if h1.val < h2.val:
                new_h = ListNode(h1.val,None)
                h1 = h1.next
            else:
                new_h = ListNode(h2.val,None)
                h2 = h2.next
        elif h1:
            new_h = ListNode(h1.val,None)
            h1 = h1.next
        elif h2:
            new_h = ListNode(h2.val,None)
            h2 = h2.next
        else:
            new_h=None
            print("here")
        real_h.next = new_h
        while h1 and h2:
            if h1.val < h2.val:
                new_h.next = ListNode(h1.val,None)
                h1 = h1.next
                new_h = new_h.next
            else:
                new_h.next = ListNode(h2.val,None)
                h2 = h2.next
                new_h = new_h.next
        if h1:
            new_h.next = h1
        if h2:
            new_h.next =h2
        return real_h.next
    
    

        


      