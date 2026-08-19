# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
      
        new = ListNode(0,None)
        cur = new
        while l1 and l2:
            if l1.val + l2.val + (flag* 1) >= 10:
                cur.next = ListNode((l1.val + l2.val + (flag* 1))%10)
                flag = True
            else:
                cur.next = ListNode((l1.val + l2.val + (flag*1)))
                flag = False
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
                if l1.val + flag*1 >= 10:
                    cur.next = ListNode((l1.val+ (flag* 1))%10)
                    flag = True

                    cur = cur.next
                else:
                    cur.next = ListNode((l1.val+ (flag* 1)))
                    cur = cur.next
                    flag = False
                l1 = l1.next
        while l2:
                if l2.val + flag*1 >= 10:
                    cur.next = ListNode((l2.val+ (flag* 1))%10)
                    flag = True

                    cur = cur.next
                else:
                    cur.next = ListNode((l2.val+ (flag* 1)))
                    cur = cur.next
                    flag = False
                l2 = l2.next
        if flag:
             cur.next = ListNode(1)
        return new.next



                    


                        

                        
                